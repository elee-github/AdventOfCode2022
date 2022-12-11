from copy import deepcopy

monkeyDict = {}
numMonkeys = 0
bigMod = 1

#input
with open("inputs/day11input") as file:
    curMonkey = None

    line = file.readline().strip()
    while line != "EOF":
        line = line.replace(':', '').split(" ")
        match line:
            case ["Monkey", *id]:
                id = int(id[0])
                monkeyDict[id] = {}
                monkeyDict[id]["active"] = 0
                curMonkey = id
                numMonkeys += 1
            case ["Starting", _, *items]:
                items = [int(i.replace(",", "")) for i in items]
                monkeyDict[curMonkey]["items"] = items
            case ["Operation", *expr]:
                _, _, oper1, oprand, oper2 = expr
                monkeyDict[curMonkey]["op"] =  compile(oper1 + " " + oprand + " " + oper2, "<string>", 'eval')
            case ["Test", *expr]:
                _, _, divisor = expr
                monkeyDict[curMonkey]["div"] = int(divisor)
                bigMod *= int(divisor)
            case ["If", "true", *expr]:
                _, _, _, id = expr
                monkeyDict[curMonkey]["if_true"] = int(id)
            case ["If", "false", *expr]:
                _, _, _, id = expr
                monkeyDict[curMonkey]["if_false"] = int(id)

        line = file.readline().strip()

def part1():
    for _ in range(20):
        for i in range(numMonkeys):
            monkey = monkeyDict[i]
            while monkey["items"]: 
                old = monkey["items"].pop(0)
                new = eval(monkey["op"])
                if new % monkey["div"] == 0:
                    monkeyDict[monkey["if_true"]]["items"].append(new)
                else:
                    monkeyDict[monkey["if_false"]]["items"].append(new)
                monkey["active"] += 1

    sorted_active = [monkeyDict[id]["active"] for id in monkeyDict]
    sorted_active.sort(reverse=True)
    return (sorted_active[0] * sorted_active[1])

def part2():
    for x in range(10000):
        for i in range(numMonkeys):
            monkey = monkeyDict[i]
            while monkey["items"]: 
                old = monkey["items"].pop(0)
                new = eval(monkey["op"])
                if new % monkey["div"] == 0:
                    monkeyDict[monkey["if_true"]]["items"].append(new % bigMod)
                else:
                    monkeyDict[monkey["if_false"]]["items"].append(new % bigMod)
                monkey["active"] += 1

    sorted_active = [monkeyDict[id]["active"] for id in monkeyDict]
    sorted_active.sort(reverse=True)
    return (sorted_active[0] * sorted_active[1])

originalMonkeyDict = deepcopy(monkeyDict)
print(part1())
monkeyDict = originalMonkeyDict
print(part2())

