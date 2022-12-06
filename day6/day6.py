i = 1
part1String = ""
part2String = ""
part1First = True
part2First = True

with open("inputs/day6input") as file:
  while True:
    chr = file.read(1)
    if not chr:
        break

    part1String += chr
    part2String += chr
    if len(part1String) > 4:
        part1String = part1String[1:]

    if len(part2String) > 14:
            part2String = part2String[1:]
    
    if len(part1String) == len(set(part1String)) == 4 and part1First:
        print(i)
        part1First = False

    if len(part2String) == len(set(part2String)) == 14 and part2First:
        print(i)
        part2First = False
    
    i += 1
    
