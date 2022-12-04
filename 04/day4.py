######################################################
### Author: Sarah Smallwood
### Advent of Code Day 4
### Date: 12/04/2022
######################################################

# Read the file in one row at a time
with open("input.txt") as f:
    lines = f.readlines()

### Part 1 ###
# Initialize number of occurrences to 0
occurrences = 0

for line in lines:
    # Initialize counter trigger to false
    happens = False

    # Split line into 1st elf's and 2nd elf's assigned tasks
    first_assignment = line.split(",")[0]
    second_assignment = line.split(",")[1]

    # Split each elf's tasks into first and last assigned tasks
    first_elf_first_task = first_assignment.split("-")[0]
    first_elf_last_task = first_assignment.split("-")[1]

    second_elf_first_task = second_assignment.split("-")[0]
    second_elf_last_task = second_assignment.split("-")[1]

    # Check to see if the first elf's tasks are encompassed in the second elf's tasks
    if int(first_elf_first_task) >= int(second_elf_first_task):
        if int(first_elf_last_task) <= int(second_elf_last_task):
            # Flag this as an occurrence
            happens = True

    # Check to see if the second elf's tasks are encompassed in the first elf's tasks
    if int(second_elf_first_task) >= int(first_elf_first_task):
        if int(second_elf_last_task) <= int(first_elf_last_task):
            # Flag this as an occurrence
            happens = True

    # If this assignment pair was flagged, add it to the total count
    if happens == True:
        occurrences = occurrences + 1

print("One elf's chores completely overlap the other "+str(occurrences)+" times.")


### Part 2 ###
occurrences = 0

for line in lines:
    # Initialize counter trigger to false
    happens = False

    # Split line into 1st elf's and 2nd elf's assigned tasks
    first_assignment = line.split(",")[0]
    second_assignment = line.split(",")[1]

    # Split each elf's tasks into first and last assigned tasks
    first_elf_first_task = first_assignment.split("-")[0]
    first_elf_last_task = first_assignment.split("-")[1]

    second_elf_first_task = second_assignment.split("-")[0]
    second_elf_last_task = second_assignment.split("-")[1]

    # Check to see if the first elf's tasks overlap with the second elf's tasks
    if int(first_elf_first_task) >= int(second_elf_first_task) and int(first_elf_first_task) <= int(second_elf_last_task):
        # Flag this as an occurrence
        happens = True

    # Check to see if the second elf's tasks overlap with the firstelf's tasks
    if int(second_elf_first_task) >= int(first_elf_first_task) and int(second_elf_first_task) <= int(first_elf_last_task):
        # Flag this as an occurrence
        happens = True

    # If this assignment pair was flagged, add it to the total count
    if happens == True:
        occurrences = occurrences + 1

print("One elf's chores at least partially overlap the other "+str(occurrences)+" times.")