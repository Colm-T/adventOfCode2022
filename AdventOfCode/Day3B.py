# Part B adds the issue that elves in squads of 3 have identical badges within their rucksacks,
# Each set of 3 rucksacks in succession are in a squad. i.e. the first 3 rucksacks, the following 3 and so on,
# Identify which item is shared within the 3 rucksacks to find which is the badge,
# Go through each squad and sum up the priorities for each squad badge. i.e. only count each badge once per squad

def get_badge_priority(badge):
    (squad_badge, ) = badge # tuple to extract single value from set
    squad_badge_priority = ord(squad_badge)

    if squad_badge_priority > 64 and squad_badge_priority < 91: # Capital letters
        squad_badge_priority -= 38 # offset to make A = 27, etc.
    elif squad_badge_priority > 96 and squad_badge_priority < 123:
        squad_badge_priority -= 96 # offset to make a = 1
    return squad_badge_priority


with open("input/day3.txt", "r") as f:
    squad_count = 0
    summed_badge_priorities = 0

    for line in f.readlines():
        squad_count += 1
        sanitized_line = line.strip()
        if squad_count == 1:
            first_rucksack = set(sanitized_line)
        elif squad_count == 2:
            second_rucksack = set(sanitized_line)
        elif squad_count == 3:
            third_rucksack = set(sanitized_line)
            squad_badge = set.intersection(first_rucksack, second_rucksack, third_rucksack)
            squad_badge_priority = get_badge_priority(squad_badge)
            summed_badge_priorities += squad_badge_priority
            squad_count = 0

print(summed_badge_priorities) # 2689
