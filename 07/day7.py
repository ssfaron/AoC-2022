######################################################
### Author: Sarah Smallwood
### Advent of Code Day 7
### Date: 12/07/2022
######################################################
import pprint

# Read the file in one row at a time
with open("input.txt") as f:
    lines = f.readlines()

dirs = {}
file_sizes = []
total_file_size = 0

### Part 1 ###
for i in range(0,len(lines)):
    # This is a command
    if lines[i].split(" ")[0] == "$":
        ls_flag = False
        if lines[i].split(" ")[1] == "cd":
            if "." not in lines[i].split(" ")[2]:
                pwd = lines[i].split(" ")[2][:-1]
                if pwd not in dirs:
                    dirs[pwd] = []
            else:
                # Find index of current working directory in dirs
                if pwd in dirs:
                    index = list(dirs).index(pwd)
                if lines[i].split(" ")[2] == ".":
                    pwd = list(dirs)[index-1]
                if lines[i].split(" ")[2] == "..":
                    pwd = list(dirs)[index-1]
        if lines[i].split(" ")[1] == "ls\n":
            ls_flag = True
    else:
        if ls_flag == True:
            content = lines[i][:-1]
            dirs[pwd].append(content)

for dir in list(dirs):
    total_file_size = 0
    #print(dir)
    values = []
    values = dirs[dir]
    for i in range(0, len(values)):
        if values[i].split(" ")[0] != "dir":
            total_file_size = total_file_size + int(values[i].split(" ")[0])
            #print(int(values[i].split(" ")[0]))
    file_sizes.append(total_file_size)


#print(file_sizes)
sum = 0
small_files = []
for size in file_sizes:
    if size <= 100000:
        small_files.append(size)
        sum = sum + size
print(sum)
total = 0
for file in small_files:
    total = total+file
print(total)
pprint.pprint(dirs)

### Part 2 ###