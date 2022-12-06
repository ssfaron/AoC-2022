######################################################
### Author: Sarah Smallwood
### Advent of Code Day 6
### Date: 12/06/2022
######################################################
import sys

# Read the file in one row at a time
with open("input.txt") as f:
    input = f.read()

### Part 1 ###
# Loop through the whole string taking 4 characters at a time starting at index 0
for i in range(0, len(input)):
    locality = input[i:i+4]

    # If all the values in the set are unique, record the index of the next value and quit
    if (len(set(locality)) == len(locality)):
        print(locality)
        character = i+4
        print(character)
        sys.exit()

### Part 2 ###
# Loop through the whole string taking 14 characters at a time starting at index 0
for i in range(0, len(input)):
    locality = input[i:i+14]

    # If all the values in the set are unique, record the index of the next value and quit
    if (len(set(locality)) == len(locality)):
        print(locality)
        character = i+14
        print(character)
        sys.exit()