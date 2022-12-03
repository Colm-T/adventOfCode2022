# In case the elf with the most calories of food on them runs out of snacks,
# Part B wants to check the top three elves, so they have 2 backups,
# So find the top 3 elves and sum their calories for the answer. [Same input]

with open("input/day1.txt", "r") as f:
    highest_calories = 0
    second_highest_calories = 0
    third_highest_calories = 0
    caloric_sum = 0
    for line in f.readlines():
        current_food = line.strip()
        if current_food:
            print(current_food)
            caloric_sum += int(current_food)
        else:
            print(f"comparing {highest_calories} against {caloric_sum}")
            if highest_calories < caloric_sum:
                third_highest_calories = second_highest_calories
                second_highest_calories = highest_calories
                highest_calories = caloric_sum
                print(highest_calories)
            caloric_sum = 0
print("=========================")
print(highest_calories)
print(second_highest_calories)
print(third_highest_calories)

print(highest_calories + second_highest_calories + third_highest_calories) # it is not 202006, which is too low