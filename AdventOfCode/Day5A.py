# https://adventofcode.com/2022/day/5
# Day 5 involves a giant cargo crane and marked crates, the input is a text doc illustrating
# how the crates are arranged in different stacks and also the series of instructions the crane will follow.
# In the instructions crates are moved from stack to stack one at a time,
# Find which crates will be on the top of each stack after all of the instructions have been completed.

stack_map = {}

def reverse_stacks(stack_map):
    for stack in stack_map:
        stack_map[stack].reverse()

def move_crates(number_of_blocks, donating_stack, receiving_stack):
    for each_block in range(number_of_blocks):
        crate = stack_map[donating_stack].pop()
        stack_map[receiving_stack].append(crate)

def convert_input_to_stacks(text_file):
    instruction_index = 0
    for line_index, line in enumerate(text_file):
        for index, character in enumerate(line):
            if ((index+3) % 4) == 0:
                if character != " " and ord(character) > 64 and ord(character) < 91:
                    stack_id = int((index+3)/4)
                    if stack_id in stack_map:
                        stack_map[stack_id].append(character)
                    else:
                        stack_map[stack_id] = list(character)
        if line == "\n":
            instruction_index = line_index + 1
            break
        
    reverse_stacks(stack_map)
    return instruction_index

def simplify_crane_instructions(line):
    return [int(character) for character in line.split() if character.isdigit()]

with open("input/day5.txt", "r") as f:
    text_file = f.readlines()
    instruction_index = convert_input_to_stacks(text_file)
    for line in text_file[instruction_index:]:
        number_of_blocks, donating_stack, receiving_stack = simplify_crane_instructions(line)
        move_crates(number_of_blocks, donating_stack, receiving_stack)
    
    top_crates = ""
    for i in range(1, len(stack_map)+1):
        top_crates += stack_map[i].pop()
    print(top_crates) # CNSZFDVLJ