# https://adventofcode.com/2022/day/6
# For day 6 we are given an input which is a string of random characters,
# We have to find how many letters we have to go through before we find 4 consecutive letters
# that are unique.

def check_for_duplicates(sequence):
    if len(set(sequence)) == 4:
        return True
    else:
        return False

with open("input/day6.txt", "r") as f:
    text = f.read()
    left_index = 0
    right_index = 3
    while right_index < len(text):
        if check_for_duplicates(text[left_index:right_index+1]):
            print(right_index+1) #1531
            break
        else:
            left_index += 1
            right_index += 1
        