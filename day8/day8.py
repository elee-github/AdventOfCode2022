field = []
with open("inputs/day8input") as file:
    line = file.readline().strip()
    while line != "EOF":
        field.append([int(i) for i in line])
        line = file.readline().strip()

def part1(field):
    total_sum = 0
    seen = set()

    for i in range(len(field)):
        cur_max = -1
        for j in range(len(field[i])):
            coord = (i, j)
            if field[i][j] > cur_max and coord not in seen:
                total_sum += 1
                seen.add(coord)

            cur_max = max(cur_max, field[i][j])
            

    for i in range(len(field)):
        cur_max = -1
        for j in range(len(field[i]) - 1, -1, -1):
            coord = (i, j)
            if field[i][j] > cur_max and coord not in seen:
                total_sum += 1
                seen.add(coord)

            cur_max = max(cur_max, field[i][j])

    for i in range(len(field[0])):
        cur_max = -1
        for j in range(len(field)):
            coord = (j, i)
            if field[j][i] > cur_max and coord not in seen:
                total_sum += 1
                seen.add(coord)

            cur_max = max(cur_max, field[j][i])

    for i in range(len(field[0])):
        cur_max = -1
        for j in range(len(field) - 1, -1, -1):
            coord = (j, i)
            if field[j][i] > cur_max and coord not in seen:
                total_sum += 1
                seen.add(coord)

            cur_max = max(cur_max, field[j][i])

    return total_sum

def part2(field):
    max_scene = 0

    for i in range(1, len(field)):
        for j in range(1, len(field[i])):
            cur_i = i
            cur_j = j
            cur_scene = 0
            total_scene = 1
            dist = 0

            while (cur_i > 0):
                cur_i -= 1
                dist += 1
                cur_scene += 1
                if field[cur_i][j] >= field[i][j]:
                    break

            cur_i = i
            cur_j = j
            total_scene *= cur_scene
            cur_scene = 0
            dist = 0

            while (cur_i < len(field) - 1):
                cur_i += 1
                dist += 1
                cur_scene += 1
                if field[cur_i][j] >= field[i][j]:
                    break

            cur_i = i
            cur_j = j
            total_scene *= cur_scene
            cur_scene = 0
            dist = 0

            while (cur_j > 0):
                cur_j -= 1
                dist += 1
                cur_scene += 1
                if field[i][cur_j] >= field[i][j]:
                    break

            cur_i = i
            cur_j = j
            total_scene *= cur_scene
            cur_scene = 0
            dist = 0

            while (cur_j < len(field[i]) - 1):
                cur_j += 1
                dist += 1
                cur_scene += 1
                if field[i][cur_j] >= field[i][j]:
                    break

            cur_i = i
            cur_j = j
            total_scene *= cur_scene
            cur_scene = 0
            dist = 0

            max_scene = max(total_scene, max_scene)

    return max_scene


print(part1(field))
print(part2(field))


'''
def part2(field):
    lr_scene = [[0 if j == 0 else 1 for j in range(len(field[i]))] for i in range(len(field))]
    rl_scene = [[0 if j == len(field[i]) - 1 else 1 for j in range(len(field[i]))] for i in range(len(field))]
    ud_scene = [[0 if i == 0 else 1 for j in range(len(field[i]))] for i in range(len(field))]
    du_scene = [[0 if i == len(field) - 1 else 1 for j in range(len(field[i]))] for i in range(len(field))]
    
    for i in range(1, len(field)):
        cur_max = field[i][0]
        max_j = 0
        for j in range(1, len(field[i])):
            if field[i][j] > cur_max:
                lr_scene[i][j] = lr_scene[i][max_j] + (j - max_j)
                max_j = 
'''