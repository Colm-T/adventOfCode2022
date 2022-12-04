# In case the elf with the most calories of food on them runs out of snacks,
# Part B wants to check the top three elves, so they have 2 backups,
# So find the top 3 elves and sum their calories for the answer. [Same input]

with open("input/day1.txt", "r") as f:
    text_file = f.read()
    elf_inventories = text_file.split('\n\n')
    summed_inventories = []
    for inventory in elf_inventories:
        items = list(map(int, inventory.split('\n')))
        summed_inventories.append(sum(items))
    summed_inventories.sort()

print(summed_inventories[-1] + summed_inventories[-2] + summed_inventories[-3]) # 208437