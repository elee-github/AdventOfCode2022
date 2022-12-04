def fullOverlap(elf1, elf2):
    elf1Start, elf1End = list(map(int, elf1.split('-')))
    elf2Start, elf2End = list(map(int, elf2.split('-')))

    if (elf1Start >= elf2Start and elf1End <= elf2End) or (elf2Start >= elf1Start and elf2End <= elf1End):
        return 1
    return 0

def partialOverlap(elf1, elf2):
    elf1Start, elf1End = list(map(int, elf1.split('-')))
    elf2Start, elf2End = list(map(int, elf2.split('-')))

    if (elf1Start < elf2Start and elf1End < elf2Start) or (elf2Start < elf1Start and elf2End < elf1Start):
        return 0
    return 1


round1Pairs = 0
round2Pairs = 0

with open("inputs/day4input", "r") as file:
    line = file.readline().strip()
    while line != "EOF":
        elf1, elf2 = line.split(',')
        round1Pairs += fullOverlap(elf1, elf2)
        round2Pairs += partialOverlap(elf1, elf2)
        line = file.readline().strip()

print(round1Pairs)
print(round2Pairs)