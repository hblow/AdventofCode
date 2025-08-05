import sys 

# Input is lines on a txt file which have a sequence of numbers each
# Seems each line is at least 5 long, no guarantee though so perhaps should add a check for that
# Each sequence must be only increasing or decreasing, and the difference between subsequent entries in a line must be within 1-3(inclusive) to be considered safe
# must return(or print I suppose, no need to return) the number of safe entries

# TODO: Calculate safe entries of given txt file
#   1. Receive txt file, and process each line
#   2. Instead of storing all processed lines, check line by line for safe condition
#   3. Check whether sequence is correct, difference check is easy as we can just check abs value is within range after subtracting, checking only increasing/decreasing may be harder
#   4. Since python has variable length integers, getting the sign bit to check may be tough. May resort to simply checking if both current and previous difference are positive or negative, if they differ, it's a violation
#   5. If one of the sequence rules is broken, break and dont add to tally, otherwise add to tally
#   6. Print and return the final tallied result
def main():
    filepath = sys.argv[1]
    res = 0
    with open(filepath, "r") as input:
        for line in input.readlines():
            report = [int(num) for num in line.split()]    # everything is seperated by whitespaces, so default split works fine, recreate it through list comprehension for int conversion
            
            if len(report) <= 1:    # for reports that have 1 entry or is empty, by default they are safe
                res += 1
                continue

            curr_diff = report[0] - report[1]     # we will uses these diffs to check for increasing or decreasing

            if not (1 <= abs(curr_diff) <= 3):     # mimics a do while loop from C, we perform the operation once, then throw it in the for loop, here if abs(curr_diff) is not within bounds, it fails
                continue 
            
            for i in range(1, len(report) - 1):
                prev_diff = curr_diff    # note, since ints are immutable, this is a copy, not a reference to curr_diff's value
                curr_diff = report[i] - report[i + 1]
                if not (1 <= abs(curr_diff) <= 3):
                    res -= 1    # I did think about using a flag as it would be less janky, but effectively it reduces res by 1 here so when we add it back later it cancels out
                    break
                if curr_diff > 0 and prev_diff > 0:    # check if curr_diff and prev_diff are the same sign, if not it is not monotonically increasing/decreasing
                    pass
                elif curr_diff < 0 and prev_diff < 0:
                    pass
                else:
                    res -= 1
                    break

            res += 1    # if no failures caught, add 1 to res

    print(res)
    return res

main()