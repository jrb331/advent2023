with open("input", "r") as f:
    lines = f.readlines()

maxDict = {
    "red": 12,
    "green": 13,
    "blue": 14
}
# counter = 0
# for line in lines:
#     splitGameNumber = line.split(':')
#     number = int(splitGameNumber[0].replace('Game ', ''))
#     print(f"Game number: {number}")
#     allTurns = splitGameNumber[1].split(';')
#     badBunches = 0
#     for turn in allTurns:
#         turnDict = {}
#         print(turn)
#         colors = turn.split(',')
#         for color in colors:
#             color = color.strip()
#             splitAgain = color.split(' ')
#             turnDict[splitAgain[1]] = int(splitAgain[0])
#         for key in turnDict:
#             if turnDict[key] > maxDict[key]:
#                 print(f"{turnDict[key]} is greater than the max of {maxDict[key]} for {key}")
#                 badBunches += 1
#     if badBunches == 0:
#         counter += number
#     print(badBunches)
# print(counter)

counter = 0
for line in lines:
    power = 1
    splitGameNumber = line.split(':')
    number = int(splitGameNumber[0].replace('Game ', ''))
    print(f"Game number: {number}")
    allTurns = splitGameNumber[1].split(';')
    badBunches = 0
    minDict = {}
    for turn in allTurns:
        turnDict = {}
        colors = turn.split(',')
        for color in colors:
            color = color.strip()
            splitAgain = color.split(' ')
            turnDict[splitAgain[1]] = int(splitAgain[0])
        # print(f"turnDict: {turnDict}")
        for key in turnDict:
            if key not in minDict:
                minDict[key] = turnDict[key]
            if turnDict[key] > minDict[key]:
                minDict[key] = turnDict[key]
    for key in minDict:
        power *= minDict[key]
    print(f"minDict: {minDict}")
    print(power)
    counter += power
print(counter)