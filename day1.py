f = open("day1input", "r")
line = f.readline()
cur_elf = 0
elves = []

while line != "EOF":
    if (line == "\n"):
        elves.append(cur_elf)
        cur_elf = 0
    else:
        cur_elf += int(line)
    
    line = f.readline()

elves.sort(reverse=True)


print(elves[0] + elves[1] + elves[2])