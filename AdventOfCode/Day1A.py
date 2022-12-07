# https://adventofcode.com/2022/day/1
# Day1A.txt is the input, a list describing how many foods each elf has brought and how much calories each food offers
# each elf's inventory is separated by a blank line. i.e. [1000\n, 2000\n, 3000\n, \n, 4000\n] 
# This would signify 2 elves with the first one having 6000 and the second having 4000

# Part A is find the elf carrying the most calories and how many total calories is that elf carrying?

with open("input/day1.txt", "r") as f:
    text_file = f.read()
    elf_inventories = text_file.split('\n\n')
    summed_inventories = []
    for inventory in elf_inventories:
        items = list(map(int, inventory.split('\n')))
        summed_inventories.append(sum(items))
print(max(summed_inventories)) # 69795 highest calories held by an elf
