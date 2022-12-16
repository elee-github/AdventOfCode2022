part1Map = {}

class flow:
    def __init__(self, curFlow, visited):
        self.curFlow = curFlow
        self.visited = visited.copy()

    def __int__(self):
        return self.curFlow


with open("inputs/day16input") as file:
    line = file.readline().strip()
    while line != "EOF":
        line = line.split(" ")
        match line:
            case [_, name, _, _, rate, _, _, _, _, *valves]:
                part1Map[name] = {}
                part1Map[name]["rate"] = int(rate.strip("rate=;"))
                part1Map[name]["children"] = [valve.strip(",") for valve in valves]
                part1Map[name]["dp"] = [flow(-1, set()) for _ in range(30)]

        line = file.readline().strip()


def part1():
    part1Map["AA"]["dp"][29] = flow(0, set())

    for curTime in range(29, 0, -1):
        for curNode in part1Map:
            curMapping = part1Map[curNode]
            curFlow = curMapping["dp"][curTime]
            if int(curFlow) == -1:
                continue

            for child in curMapping["children"]:
                part1Map[child]["dp"][curTime - 1] = max(curFlow, part1Map[child]["dp"][curTime - 1], key=int)

            nextSelfFlow = part1Map[curNode]["dp"][curTime - 1]
            if curNode not in curFlow.visited:
                newFlow = flow(int(curFlow) + (curMapping["rate"] * curTime), curFlow.visited)
                newFlow.visited.add(curNode)
                part1Map[curNode]["dp"][curTime - 1] = max(nextSelfFlow, newFlow, key=int)
            else:
                part1Map[curNode]["dp"][curTime - 1] = max(nextSelfFlow, curFlow, key=int)
    
    maxFlow = -1
    for curNode in part1Map:
        maxFlow = max(int(part1Map[curNode]["dp"][0]), maxFlow)

    return maxFlow

print(part1())



print("$$$$", end=" ")
for curNode in part1Map:
    print(curNode.ljust(4), end=" ")
print("")
for curTime in range(29, -1, -1):
    print(str(30-curTime).ljust(3), end=": ")
    for curNode in part1Map:
        print(str(int(part1Map[curNode]["dp"][curTime])).ljust(4), end=" ")
    print("")