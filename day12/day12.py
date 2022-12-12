array = []
startR = startC = endR = endC = None

with open("inputs/day12input") as file:
    line = file.readline().strip()
    row = 0
    while line != "EOF":
        if "S" in line:
            startC = line.index("S")
            startR = row
            line = line.replace("S", "a")
        if "E" in line:
            endC = line.index("E")
            endR = row
            line = line.replace("E", "z")

        array.append(line)
        row += 1

        line = file.readline().strip()

def bfsPart1():
    coordQ = [(startR, startC)]
    distQ = [0]
    visited = set()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while coordQ:
        curR, curC = coordQ.pop(0)
        curDist = distQ.pop(0)

        if (curR, curC) in visited:
            continue

        visited.add((curR, curC))
        if (curR, curC) == (endR, endC):
            return curDist

        for xDir, yDir in dirs:
            newR = curR + xDir
            newC = curC + yDir
            if newR in range(0, len(array)) and newC in range(0, len(array[newR])) and ord(array[newR][newC]) <= ord(array[curR][curC]) + 1:
                coordQ.append((newR, newC))
                distQ.append(curDist + 1)


def bfsPart2():
    coordQ = [(endR, endC)]
    distQ = [0]
    visited = set()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while coordQ:
        curR, curC = coordQ.pop(0)
        curDist = distQ.pop(0)

        if (curR, curC) in visited:
            continue

        visited.add((curR, curC))
        if array[curR][curC] == "a":
            return curDist

        for xDir, yDir in dirs:
            newR = curR + xDir
            newC = curC + yDir
            if newR in range(0, len(array)) and newC in range(0, len(array[newR])) and ord(array[newR][newC]) >= ord(array[curR][curC]) - 1:
                coordQ.append((newR, newC))
                distQ.append(curDist + 1)


print(bfsPart1())
print(bfsPart2())




