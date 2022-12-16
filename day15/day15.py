snbList = []

with open("inputs/day15input") as file:
    line = file.readline().strip()
    while line != "EOF":
        line = line.split()
        senC, senR, beaC, beaR = [int(line[i][2:].strip(":,")) for i in range(len(line)) if i in [2, 3, 8, 9]]
        snbList.append([senR, senC, beaR, beaC])

        line = file.readline().strip()

def mannDist(inList):
    return abs(inList[0] - inList[2]) + abs(inList[1] - inList[3])

def part1():
    PART1ROW = 2000000
    noBeacon = set()

    for snb in snbList:
        dist = mannDist(snb)
        senR, senC, beaR, beaC = snb
        width = dist - abs(senR - PART1ROW)
        for i in range(senC - width, senC + width + 1):
            if i == beaC and PART1ROW == beaR:
                continue
            noBeacon.add(i)

    return len(noBeacon)

def isBeacon(r, c):
    for snb in snbList:
        senR, senC, _, _ = snb
        dist1 = mannDist(snb)
        dist2 = mannDist([senR, senC, r, c])
        if dist2 <= dist1:
            return False

    return True

def part2():
    PART2MAX = 4000000

    for snb in snbList:
        dist = mannDist(snb)
        senR, senC, beaR, beaC = snb
        edge = []
        curR = senR - dist
        curC = senC
        dirR = dirC = 1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        first = True

        while first or (curR, curC) != (senR - dist, senC):
            first = False
            for cdr, cdc in dirs:
                checkR, checkC = curR + cdr, curC + cdc
                if checkR < 0 or checkR >= PART2MAX + 1 or checkC < 0 or checkC >= PART2MAX + 1:
                    continue
                if isBeacon(checkR, checkC):
                    return checkR + checkC * 4000000

            curR += dirR
            curC += dirC

            if curR == senR + dist:
                dirR = -1
            elif curR == senR - dist:
                dirR = 1

            if curC == senC + dist:
                dirC = -1
            elif curC == senC - dist:
                dirC = 1

    return "FAIL"

                


        
            


print(part1())
print(part2())
