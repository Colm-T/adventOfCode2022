# Part 2 is the same as part 4 but instead of 4 consecutive unique letters, 
# it must be 14 consecutive unique letters


def check_for_duplicates(sequence):
    if len(set(sequence)) == 14:
        return True
    else:
        return False

with open("input/day6.txt", "r") as f:
    text = f.read()
    left_index = 0
    right_index = 13
    while right_index < len(text):
        if check_for_duplicates(text[left_index:right_index+1]):
            print(right_index+1) # 2518
            break
        else:
            left_index += 1
            right_index += 1