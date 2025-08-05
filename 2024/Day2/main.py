import sys 

# Input is lines on a txt file which have a sequence of numbers each
# Seems each line is at least 5 long, no guarantee though so perhaps should add a check for that
# Each sequence must be only increasing or decreasing, and the difference between subsequent entries in a line must be within 1-3(inclusive) to be considered safe
# must return(or print I suppose, no need to return) the number of safe entries

# TODO: (PART 1) Calculate safe entries of given txt file
#   1. Receive txt file, and process each line
#   2. Instead of storing all processed lines, check line by line for safe condition
#   3. Check whether sequence is correct, difference check is easy as we can just check abs value is within range after subtracting, checking only increasing/decreasing may be harder
#   4. Since python has variable length integers, getting the sign bit to check may be tough. May resort to simply checking if both current and previous difference are positive or negative, if they differ, it's a violation
#   5. If one of the sequence rules is broken, break and dont add to tally, otherwise add to tally
#   6. Print and return the final tallied result
#
# TODO: (PART 2) Add problem dampener functionality
#   1. Add a flag I can set before running the program to activate problem dampener or not
#   2. If flag is set, should change functionality to check if a report either with the previous or current number is valid, as one of them has to go for it to be possibly safe
def main():
    res = 0
    if len(sys.argv) < 2:
        print("No filepath given, please input a filepath when running, ie. `py main.py input.txt`")
    filepath = sys.argv[1]
    damp_on = False
    if len(sys.argv) == 3 and sys.argv[2] == '--debug':
        damp_on = True
    with open(filepath, "r") as input:
        for line in input.readlines():
            report = [int(num) for num in line.split()]    # everything is seperated by whitespaces, so default split works fine, recreate it through list comprehension for int conversion
            
            if len(report) <= 1:    # for reports that have 1 entry or is empty, by default they are safe
                res += 1
                continue
            
            res += check_safe(report, damp_on)

    print(res)
    return res

# Helper function for calculating if a report is safe or not, if damp_on is true, then it applies part 2 checks
def check_safe(report, damp_on):
    res = 0
    curr_diff = None
    for i in range(0, len(report) - 1):
        prev_diff = curr_diff    # note, since ints are immutable, this is a copy, not a reference to curr_diff's value
        curr_diff = report[i] - report[i + 1]
        if not (1 <= abs(curr_diff) <= 3):
            if damp_on:
                res += max(check_safe(report[:i] + report[i + 1:], False),check_safe(report[:i + 1] + report[i+2:], False))
                return res
            else:
                res -= 1    # I did think about using a flag as it would be less janky, but effectively it reduces res by 1 here so when we add it back later it cancels out
                break
        if prev_diff == None:    # if prev_diff is not set yet, ignore it
            pass
        elif curr_diff > 0 and prev_diff > 0:    # check if curr_diff and prev_diff are the same sign, if not it is not monotonically increasing/decreasing
            pass
        elif curr_diff < 0 and prev_diff < 0:
            pass
        else:
            if damp_on:
                # extra check here, since if we are only past the starting index, the previous element may be involved in the breaking the monotonic sequence, so much check the 0th index
                if i == 1:
                    res += max(check_safe(report[:i-1] + report[i:], False), check_safe(report[:i] + report[i + 1:], False), check_safe(report[:i + 1] + report[i+2:], False))
                else:
                    res += max(check_safe(report[:i] + report[i + 1:], False), check_safe(report[:i + 1] + report[i+2:], False))
                return res
            else:
                res -= 1
                break
    res += 1
    return res

main()