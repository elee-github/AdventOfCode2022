oppMatchup = ["A", "B", "C"]
yourMatchup = ["X", "Y", "Z"]
winLoss = [0, 3, 6]

def pointsPart1(opp, you):
    oppI = oppMatchup.index(opp)
    youI = yourMatchup.index(you)

    choicePoints = youI + 1

    if (oppI == youI):
        return winLoss[1] + choicePoints
    if ((oppI + 1) % 3 == youI):
        return winLoss[2] + choicePoints
    if ((oppI + 2) % 3 == youI):                #in case lol
        return winLoss[0] + choicePoints

def pointsPart2(opp, you):
    oppI = oppMatchup.index(opp)

    if you == "Y":
        return oppI + 1 + winLoss[1]
    if you == "X":
        return ((oppI + 2) % 3) + 1 + winLoss[0]
    if you == "Z":                              #still just in case
        return ((oppI + 1) % 3) + 1 + winLoss[2]

round1Points = 0
round2Points = 0

with open("day2input", "r") as file:
    line = file.readline().strip()
    while line != "EOF":
        match = line.split(" ")
        round1Points += pointsPart1(match[0], match[1])
        round2Points += pointsPart2(match[0], match[1])
        line = file.readline().strip()



print(round1Points)
print(round2Points)