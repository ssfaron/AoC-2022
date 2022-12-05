######################################################
### Author: Sarah Smallwood
### Advent of Code Day 5
### Date: 12/05/2022
######################################################

# Crates
crates = [["H","L","R","F","B","C","J","M"],
["D","C","Z"],
["W","G","N","C","F","J","H"],
["B","S","T","M","D","J","P"],
["J","R","D","C","N"],
["Z","G","J","P","Q","D","L","W"],
["H","R","F","T","Z","P"],
["G","M","V","L"],
["J","R","Q","F","P","G","B","C"]]

# Read the file in one row at a time
with open("input.txt") as f:
    lines = f.readlines()

### Part 1 ###
for line in lines:
    words = line.split(" ")
    quantity = int(words[1])
    source = int(words[3])-1
    target = int(words[5])-1

    # Follow the instructions
    for i in range(1,quantity+1):
        top = crates[source].pop(0) # Remove a crate from the top of the source stack
        move = crates[target].insert(0,top) # Move it to the top of the target stack

# Create a vector to hold the letters representing the top of each stack
all_tops = []

for i in range(0,9):
    all_tops.append(crates[i][0])

print("The tops of all the crates are given as: "+"".join(all_tops)+".")

### Part 2 ###
# Reset Crates!!!
crates = [["H","L","R","F","B","C","J","M"],
["D","C","Z"],
["W","G","N","C","F","J","H"],
["B","S","T","M","D","J","P"],
["J","R","D","C","N"],
["Z","G","J","P","Q","D","L","W"],
["H","R","F","T","Z","P"],
["G","M","V","L"],
["J","R","Q","F","P","G","B","C"]]

for line in lines:
    words = line.split(" ")
    quantity = int(words[1])
    source = int(words[3])-1
    target = int(words[5])-1

    # Follow the instructions
    for i in range(0,quantity):
        top = crates[source].pop(0) # Remove a crate from the top of the source stack
        move = crates[target].insert(i,top) # Move it to the target stack in the order it originally was

# Create a vector to hold the letters representing the top of each stack
all_tops = []

for i in range(0,9):
    all_tops.append(crates[i][0])

print("The tops of all the crates carried in stacks are given as: "+"".join(all_tops)+".")
