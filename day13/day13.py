import functools

def cmpPacket(list1, list2):
    for i in range(max(len(list1), len(list2))):
        if i >= len(list1) and i >= len(list2):
            return 0
        elif i >= len(list1):
            return -1
        elif i >= len(list2):
            return 1

        if type(list1[i]) == list or type(list2[i]) == list:
            if(type(list1[i]) != list):
                inList1 = [list1[i]]
            else:
                inList1 = list1[i]
            if(type(list2[i]) != list):
                inList2 = [list2[i]]
            else:
                inList2 = list2[i]

            val = cmpPacket(inList1, inList2)
            if val == 0:
                i += 1
                continue
            return val
        
        if list1[i] == list2[i]:
            i += 1
            continue
        elif list1[i] < list2[i]:
            return -1
        else:
            return 1

    return 0
            

part1Total = 0
part2Packets = []
i = 1

with open("inputs/day13input") as file:
    line1 = file.readline().strip()
    line2 = file.readline().strip()
    while line1 != "EOF":
        line1 = eval(line1)
        line2 = eval(line2)

        if(cmpPacket(line1, line2) == -1):
            part1Total += i

        part2Packets.append(line1)
        part2Packets.append(line2)

        i += 1

        _ = file.readline().strip()
        line1 = file.readline().strip()
        line2 = file.readline().strip()

part2Packets.append([[2]])
part2Packets.append([[6]])
part2Packets.sort(key=functools.cmp_to_key(cmpPacket))

index1 = part2Packets.index([[2]]) + 1
index2 = part2Packets.index([[6]]) + 1

print(part1Total)
print(index1 * index2)
