def part1(comp1, comp2):
    set1 = set(comp1)
    for chara in comp2:
        if chara in set1:
            if 'A' <= chara and 'Z' >= chara:
                return ord(chara) - 65 + 27
            elif 'a' <= chara and 'z' >= chara:
                return ord(chara) - 96
            else:
                print("BAD THING")                  #should never happen
                return -9999999999

def part2(lines):
    elf1, elf2, elf3 = lines
    set1 = set(elf1)
    set2 = set(elf2)
    for chara in elf3:
        if chara in set1 and chara in set2:
            if 'A' <= chara and 'Z' >= chara:
                return ord(chara) - 65 + 27
            elif 'a' <= chara and 'z' >= chara:
                return ord(chara) - 96
            else:
                print("BAD THING")                  #should never happen
                return -9999999999

part1ans = 0
part2ans = 0

with open("inputs/day3input", "r") as file:
    line = file.readline().strip()
    lineList = []
    lineCount = 0

    while line != "EOF":
        halfLine = len(line) // 2
        part1ans += part1(line[:halfLine], line[halfLine:])

        lineCount += 1
        lineList.append(line)
        if lineCount >= 3:
            part2ans += part2(lineList)
            lineList = []
            lineCount = 0
        
        line = file.readline().strip()

print(part1ans)
print(part2ans)