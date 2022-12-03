# Day1A.txt is the input, a list describing how many foods each elf has brought and how much calories each food offers
# each elf's inventory is separated by a blank line. i.e. [1000\n, 2000\n, 3000\n, \n, 4000\n] 
# This would signify 2 elves with the first one having 6000 and the second having 4000

# Part A is find the elf carrying the most calories and how many total calories is that elf carrying?

with open("input/day1.txt", "r") as f:
    highest_calories = 0
    caloric_sum = 0
    for line in f.readlines():
        current_food = line.strip()
        if current_food:
            caloric_sum += int(current_food)
        else:
            if highest_calories < caloric_sum:
                highest_calories = caloric_sum
            caloric_sum = 0
print(highest_calories) # 69795 highest_calories held by an elf