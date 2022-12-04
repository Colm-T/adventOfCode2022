# Day 4, The elves have been given assignments to clean up the camp area, they have each been given a range of consecutive sections to clean,
# with each section having a ID number. The input this time is a text file where each line contains pairs of ranges, one for each elf of the pair.
# i.e. 2-4, 3-7. (first elf cleans sections 2,3 and 4 while second elf cleans sections 3,4,5,6 and 7)
# Find how many pairs contain an assignment that fully contains the other assignment. i.e. 2-4, 3-4.

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
        if assignment_one[0] <= assignment_two[0] and assignment_one[1] >= assignment_two[1]: # assignment_two is inside assignment_one
            redundant_assignments += 1
        elif assignment_one[0] >= assignment_two[0] and assignment_one[1] <= assignment_two[1]: # assignment_one is inside assignment_two
            redundant_assignments += 1
print(redundant_assignments) # 503



