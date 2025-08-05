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
            print(line)
    
    print(res)
    return res