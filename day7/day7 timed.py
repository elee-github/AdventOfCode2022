import timeit

class Node:
    def __init__(self, name, size, parent, is_directory):
        self.parent = parent
        self.children = []
        self.name = name
        self.size = size
        self.is_directory = is_directory

    def child_with_name(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def recursive_add(self, add_size):
        self.size += add_size
        if self.parent is not None:
            self.parent.recursive_add(add_size)

    def part1Sum(self):
        ret = 0

        if self.size <= 100000:
            ret += self.size

        for child in self.children:
            if child.is_directory:
                ret += child.part1Sum()

        return ret

    def part2Min(self, floor, curMin):
        if self.size >= floor:
            curMin = min(curMin, self.size)

        for child in self.children:
            if child.is_directory:
                res = child.part2Min(floor, curMin)
                if res >= floor:
                    curMin = min(curMin, res)
        
        return curMin




root = Node("/", 0, None, True)
curFile = root
FILESYSSIZE = 70000000
REQSTORAGE = 30000000

def main_or_smth():
    with open("inputs/day7input") as file:
        line = file.readline().strip()
        while line != "EOF":
            line = line.split(" ")

            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "/":
                        curFile = root
                    elif line[2] == "..":
                        curFile = curFile.parent
                    else:
                        curFile = curFile.child_with_name(line[2])
                elif line[1] == "ls":
                    pass
                else:
                    print("this not supposed to happen")
                    break

            #if line doesn't start with $, it's part of ls
            elif line[0] == "dir":
                newFile = Node(line[1], 0, curFile, True)
                curFile.children.append(newFile)
            else:
                newFile = Node(line[1], int(line[0]), curFile, False)
                curFile.recursive_add(int(line[0]))

            line = file.readline().strip()


    print(root.part1Sum())
    floor = REQSTORAGE - (FILESYSSIZE - root.size)
    print(root.part2Min(floor, 2 ** 32))

print(timeit.timeit(main_or_smth, number = 1))