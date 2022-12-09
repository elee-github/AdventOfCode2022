part1Set = set()

def isNegative(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0

def movement(hr, hc, tr, tc):
    safe = set()
    for i in range(hr - 1, hr + 2):
        for j in range(hc - 1, hc + 2):
            safe.add((i, j))

    rDir = isNegative(hr - tr)
    cDir = isNegative(hc - tc)

    if (tr, tc) in safe:
        return (tr, tc)
    elif tr == hr:
        return (tr, tc + cDir)
    elif tc == hc:
        return (tr + rDir, tc)
    else:
        return (tr + rDir, tc + cDir)

#part 1 vars
part1Locs = set()
hr = hc = 0
tr = tc = 0
#part 2 vars
part2Locs = set()
rope = [[0, 0] for _ in range(10)]


with open("inputs/day9input") as file:
    line = file.readline().strip()
    while line != "EOF":
        direct, dist = line.split()
        distPart1 = distPart2 = int(dist)

        #print(direct, dist)

        while distPart1 > 0:
            match direct:
                case "R":
                    hc += 1
                case "L":
                    hc -= 1
                case "U":
                    hr += 1
                case "D":
                    hr -= 1

            tr, tc = movement(hr, hc, tr, tc)
            part1Locs.add((tr, tc))
            distPart1 -= 1
            #print(hr, hc, tr, tc)

        while distPart2 > 0:
            match direct:
                case "R":
                    rope[0][0] += 1
                case "L":
                    rope[0][0] -= 1
                case "U":
                    rope[0][1] += 1
                case "D":
                    rope[0][1] -= 1

            for i in range(1, 10):
                rope[i][0], rope[i][1] = movement(rope[i - 1][0], rope[i - 1][1], rope[i][0], rope[i][1])
                if i == 9:
                    part2Locs.add((rope[i][0], rope[i][1]))

            distPart2 -= 1

        line = file.readline().strip()

print(len(part1Locs))
print(len(part2Locs))