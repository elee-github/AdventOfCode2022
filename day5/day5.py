stacks1 = [[] for i in range(9)]
stacks2 = [[] for i in range(9)]

def stacksPart1(num, fromS, toS):
    for _ in range(num):
        stacks1[toS].insert(0, stacks1[fromS].pop(0))

def stacksPart2(num, fromS, toS):
    for i in range(num - 1, -1, -1):
        stacks2[toS].insert(0, stacks2[fromS][i])

    for _ in range(num):
        stacks2[fromS].pop(0)

def stackTop():
    for stack in stacks1:
        print(stack[0], end = '')
    print('')
    for stack in stacks2:
        print(stack[0], end = '')
    print('')

#GOD I HATE STRING COMPREHENSION AHHHHHHHH
with open("inputs/day5input", "r") as file:
    line = file.readline()
    while line != "EOF":
        orgLine = line
        line = line.split(" ")
        if line[0] != 'move':
            trueI = 0
            orgLine = orgLine.replace("    ", " [.] ").strip()
            line = [i for i in orgLine.split(" ") if i != '']
            if line and line[0] and line[0][0] == '[':
                for i in range(len(line)):
                    if line[i] != '[.]':
                        stacks1[i].append(line[i].strip('[]'))
                        stacks2[i].append(line[i].strip('[]'))
        else:
            num = int(line[1])
            fromS = int(line[3]) - 1
            toS = int(line[5]) - 1

            stacksPart1(num, fromS, toS)
            stacksPart2(num, fromS, toS)
                
        line = file.readline()

stackTop()
