stone = []
grid = []
minRow = maxRow = minCol = maxCol = -1

with open("inputs/day14input") as file:
    line = file.readline().strip()
    while line != "EOF":
        line = line.split(" -> ")
        stone.append(line)
        for item in line:
            col, row = [int(i) for i in item.split(",")]

            if minRow == -1:
                minRow = 0
                maxRow = row
            elif minCol == -1:
                minCol = col
                maxCol = col
            
            minRow = min(minRow, row)
            maxRow = max(maxRow, row)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)

        line = file.readline().strip()

grid = [["." for i in range(maxCol - minCol + 1)] for j in range(maxRow - minRow + 1)]

for line in stone:
    last = None
    for item in line:
        col, row = [int(i) for i in item.split(",")]
        col -= minCol
        row -= minRow
        if last is not None:
            lastR, lastC = last
            if row - lastR:
                start = min(lastR, row)
                fin = max(lastR, row)
                for i in range(start, fin + 1):
                    grid[i][col] = "#"
            else:
                start = min(lastC, col)
                fin = max(lastC, col)
                for i in range(start, fin + 1):
                    grid[row][i] = "#"
        
        last = (row, col)

def part1():
    global maxRow

    part1Count = 0
    startC, startR = (500, 0)
    startC -= minCol
    fin = False

    while(True):
        curC, curR = startC, startR
        while(True):
            if curR + 1 >= maxRow - minRow + 1:
                fin = True
                break
            elif grid[curR + 1][curC] == ".":
                curR += 1
            elif curC - 1 < 0:
                fin = True
                break
            elif grid[curR + 1][curC - 1] == ".":
                curR += 1
                curC -= 1
            elif curC + 1 >= maxCol - minCol + 1:
                fin = True
                break
            elif grid[curR + 1][curC + 1] == ".":
                curR += 1
                curC += 1
            else:
                grid[curR][curC] = "o"
                break
        
        if fin:
            return part1Count

        part1Count += 1

def part2(part1i):
    global maxCol, maxRow
    part2Count = part1i
    startC, startR = (500, 0)
    startC -= minCol
    fin = False

    grid.append(['.' for _ in range(minCol, maxCol + 1)])
    maxRow += 1

    while(True):
        curC, curR = startC, startR
        while(True):
            if curR + 1 >= maxRow - minRow + 1:
                grid[curR][curC] = "o"
                break
            elif grid[curR + 1][curC] == ".":
                curR += 1
            elif curC - 1 < 0:
                for line in grid:
                    line.insert(0, ".")
                maxCol += 1
                startC += 1
                curR += 1
            elif grid[curR + 1][curC - 1] == ".":
                curR += 1
                curC -= 1
            elif curC + 1 >= maxCol - minCol + 1:
                for line in grid:
                    line.append(".")
                maxCol += 1
                curR += 1
                curC += 1
            elif grid[curR + 1][curC + 1] == ".":
                curR += 1
                curC += 1
            else:
                grid[curR][curC] = "o"
                break
        
        part2Count += 1

        if grid[startR][startC] == "o":
            return part2Count
        
part1o = part1()
print(part1o)
print(part2(part1o))
#[print(''.join(x)) for x in grid]


