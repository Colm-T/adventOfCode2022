# Day 3 is about loading rucksacks with supplies, each rucksack has two large compartments,
# The input is a text file with each line being a string corresponding to a rucksack, 
# with the first half of the string being the first compartment and second half being the second compartment,
# Each rucksack, has an item duplicated between the compartments, [rucksack = line, item = char, compartments = halves]
# And each item has a priority value, a to z = 1 to 26 and A to Z = 27 to 52.
# Find the duplicate in each rucksack and sum up their priorities

def compare_compartments(first_compartment, second_compartment):
    (duplicated_item, ) = first_compartment.intersection(second_compartment) # tuple to extract single value from set
    item_priority = ord(duplicated_item)

    if item_priority > 64 and item_priority < 91: # Capital letters
        item_priority -= 38 # offset to make A = 27, etc.
    elif item_priority > 96 and item_priority < 123:
        item_priority -= 96 # offset to make a = 1
    return item_priority


with open("input/day3.txt", "r") as f:
    summed_item_priorities = 0

    for line in f.readlines():
        sanitized_line = line.strip()
        first_compartment = set(sanitized_line[:len(sanitized_line)//2])
        second_compartment = set(sanitized_line[len(sanitized_line)//2:])
        summed_item_priorities += compare_compartments(first_compartment, second_compartment)

print(summed_item_priorities) # 8176
