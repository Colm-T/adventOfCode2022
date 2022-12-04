# For part 2, the elves want to know how many of the assignment pairs have any overlap at all,
# so find how many pairs have any overlap at all

with open("input/day4.txt", "r") as f:
    redundant_assignments = 0
    for line in f.readlines():
        assignment_one = []
        assignment_two = []
        assignments = [item.strip() for item in line.split(',')]
        for assignment in assignments:
            if not assignment_one:
                assignment_one = list(map(int, assignment.split('-')))
            else:
                assignment_two = list(map(int, assignment.split('-')))
        if assignment_one[0] <= assignment_two[0] and assignment_one[1] >= assignment_two[0]:
            redundant_assignments += 1
        elif assignment_one[0] <= assignment_two[1] and assignment_one[1] >= assignment_two[1]:
            redundant_assignments += 1
        elif assignment_two[0] <= assignment_one[0] and assignment_two[1] >= assignment_one[0]:
            redundant_assignments += 1
        elif assignment_two[0] <= assignment_one[1] and assignment_two[1] >= assignment_one[1]:
            redundant_assignments += 1

print(redundant_assignments) # 827

# first option: when a[0] is lower than b[0], a[1] is higher than b[0].     i.e. [4][6] [5][7]
# second option: when a[0] is lower than b[1], a[1] is higher than b[1].    i.e. [6][8] [5][7]
# third option: when b[0] is lower than a[0], b[1] is higher than a[0].     i.e. [5][7] [4][6]
# fourth option: when b[0] is lower than a[1], b[1] is higher than a[1].    i.e. [5][7] [6][8]
