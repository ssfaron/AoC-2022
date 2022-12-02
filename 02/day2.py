######################################################
### Author: Sarah Smallwood
### Advent of Code Day 2
### Date: 12/02/2022
######################################################

# Column 1 --> opponent
# A = Rock, B = Paper, C = Scissors

# Column 2 --> your move
# X = Rock (1), Y = Paper (2), Z = Scissors (3)

### Part 1 ###
rps_hands = []
total_score = 0
hand_score = 0

# Read the file in one row at a time
with open("inputs.txt") as f:
    lines = f.readlines()

# Save each hand as a vector within a larger vector
for line in lines:
    new_line = line.split(' ')
    no_breaks = new_line[1].split('\n')
    rps_hands.append([new_line[0], no_breaks[0]])

# For each vector pair, determine the appropriate points earned
for i in range(0, len(rps_hands)):
    if rps_hands[i][1] == "X":
        if rps_hands[i][0] == "A":
            hand_score = 1 + 3
        if rps_hands[i][0] == "B":
            hand_score = 1 + 0
        if rps_hands[i][0] == "C":
            hand_score = 1 + 6
    if rps_hands[i][1] == "Y":
        if rps_hands[i][0] == "A":
            hand_score = 2 + 6
        if rps_hands[i][0] == "B":
            hand_score = 2 + 3
        if rps_hands[i][0] == "C":
            hand_score = 2 + 0
    if rps_hands[i][1] == "Z":
        if rps_hands[i][0] == "A":
            hand_score = 3 + 0
        if rps_hands[i][0] == "B":
            hand_score = 3 + 6
        if rps_hands[i][0] == "C":
            hand_score = 3 + 3

    total_score = total_score + hand_score

print("The total score is: "+str(total_score)+".")


### Part 2 ###
# Reset the score back to 0!!!
total_score = 0
hand_score = 0

# For each vector pair, determine the appropriate points earned with the new definitions
for i in range(0, len(rps_hands)):
    if rps_hands[i][1] == "X":
        if rps_hands[i][0] == "A":
            hand_score = 0 + 3
        if rps_hands[i][0] == "B":
            hand_score = 0 + 1
        if rps_hands[i][0] == "C":
            hand_score = 0 + 2
    if rps_hands[i][1] == "Y":
        if rps_hands[i][0] == "A":
            hand_score = 3 + 1
        if rps_hands[i][0] == "B":
            hand_score = 3 + 2
        if rps_hands[i][0] == "C":
            hand_score = 3 + 3
    if rps_hands[i][1] == "Z":
        if rps_hands[i][0] == "A":
            hand_score = 6 + 2
        if rps_hands[i][0] == "B":
            hand_score = 6 + 3
        if rps_hands[i][0] == "C":
            hand_score = 6 + 1

    total_score = total_score + hand_score

print("The total score is: "+str(total_score)+".")