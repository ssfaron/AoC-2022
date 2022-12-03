######################################################
### Author: Sarah Smallwood
### Advent of Code Day 3
### Date: 12/03/2022
######################################################

### Functions ###
# Find the matching item in rucksacks 1 and 2
def check_item(rucksack1, rucksack2):
    for i in range(0, len(rucksack1)):
        for j in range(0, len(rucksack2)):
            if rucksack1[i] == rucksack2[j]:
                item.append(rucksack1[i])
                return

# Find the matching item in rucksacks 1, 2, and 3
def check_group_item(rucksack1, rucksack2, rucksack3):
    for i in range(0, len(rucksack1)):
        if rucksack1[i] in rucksack2:
            if rucksack1[i] in rucksack3:
                item.append(rucksack1[i])
                return

### Common Code ###
# Read the file in one row at a time
with open("input.txt") as f:
    lines = f.readlines()

### Part 1 ###
item = []

# Split the input into rucksacks 1 and 2
for line in lines:
    rucksack1 = []
    rucksack2 = []

    length = len(line)-1
    for i in range(0,int(length/2)):
        rucksack1.append(line[i])
    for i in range(int(length/2), length):
        rucksack2.append(line[i])

    # Find the matching item
    check_item(rucksack1, rucksack2)

# Initialize total priority value to 0
total_priority = 0

# Calculate the total priority value by converting the character to an ascii value and converting the ascii to decimal
for i in item:
    if i.isupper() == False:
        total_priority = total_priority + (ord(i)-96)
    if i.isupper() == True:
        total_priority = total_priority + (ord(i)-38)

print("The total priority is: "+str(total_priority)+".")

### Part 2 ###
item = []
lines_vector = []

# Save input to a vector
for line in lines:
    lines_vector.append(line)

# Split the input into rucksacks 1, 2, and 3
for i in range(0, int(len(lines)/3)):
    rucksack1 = lines_vector[0]
    rucksack2 = lines_vector[1]
    rucksack3 = lines_vector[2]

    # Pop the top 3 lines of the input off the stack
    lines_vector.pop(0)
    lines_vector.pop(0)
    lines_vector.pop(0)

    # Find the matching item amongst the 3 bags
    check_group_item(rucksack1, rucksack2, rucksack3)

# Initialize total priority value to 0
total_priority = 0

# Calculate the total priority value by converting the character to an ascii value and converting the ascii to decimal
for i in item:
    if i.isupper() == False:
        total_priority = total_priority + (ord(i)-96)
    if i.isupper() == True:
        total_priority = total_priority + (ord(i)-38)

print("The total priority is: "+str(total_priority)+".")



