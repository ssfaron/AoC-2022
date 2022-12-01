######################################################
### Author: Sarah Smallwood
### Advent of Code Day 1
### Date: 12/01/2022
######################################################

### Part 1 ###
input = "part1_input.txt"
total_calories = 0
most_calories = 0

# Read in the input file
with open(input) as f:
    lines = f.readlines()

for line in lines:
    # Count up all the consecutive calorie inputs
    if line != "\n":
        total_calories = total_calories + int(line)
    # If the sum of the calories is greater than the most on record, replace the record
    if line == "\n":
        if total_calories > most_calories:
            most_calories = total_calories
        # Reinitialize the total calories to 0 for the next elf
        total_calories = 0

print("The most number of calories is: "+str(most_calories))


### Part 2 ###
# Repeat Part 1 but save all the totals to a list, sort the list, and sum the top 3

input = "part1_input.txt"
total_calories = 0
most_calories = 0
calorie_list = []

# Read in the input file
with open(input) as f:
    lines = f.readlines()

for line in lines:
    # Count up all the consecutive calorie inputs
    if line != "\n":
        total_calories = total_calories + int(line)
    # Reinitialize the total calories to 0 for the next elf
    if line == "\n":
        calorie_list.append(total_calories)
        total_calories = 0

calorie_list.sort(reverse = True)
top_3 = calorie_list[0] + calorie_list[1] + calorie_list[2]

print("The sum of the top 3 calorie earners is: "+str(top_3))