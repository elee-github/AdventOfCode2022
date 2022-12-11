toExecute = []
curExecute = None
cyclesLeft = 0
signalIndx = 1
curSignal = 1
read = True
part1Total = 0
part2String = ""


with open("inputs/day10input") as file:
    line = file.readline().strip()
    while read or toExecute or curExecute:
        if line == "EOF":
            read = False
        else:
            line = line.split(" ")

            match line[0]:
                case "noop":
                    toExecute.append(None)
                case "addx":
                    toExecute.append(int(line[1]))

        if cyclesLeft == 0:
            curExecute = toExecute.pop(0)
            if curExecute is None:
                cyclesLeft = 1
            else:
                cyclesLeft = 2

        #print("During:", signalIndx)
        #print(curSignal, end="; ")
        #print(toExecute, curExecute)

        if (signalIndx - 1) % 40 == 0 and signalIndx != 1:
            part2String += "\n"
        
        if (signalIndx - 1) % 40 in range(curSignal - 1, curSignal + 2):
            part2String += "#"
        else:
            part2String += "."

        if signalIndx % 40 == 20:
            #print(signalIndx, curSignal)
            part1Total += curSignal * signalIndx
        
        cyclesLeft -= 1
        if curExecute and cyclesLeft == 0:
            curSignal += curExecute
            curExecute = None

        #print("End:", signalIndx)
        #print(curSignal)
        
        signalIndx += 1

        if read:
            line = file.readline().strip()

print(part1Total)
print(part2String)