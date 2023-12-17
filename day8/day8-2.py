import math
with open("input.txt", "r") as f:
    lines = f.readlines()
    pattern = list(lines[0].strip())
    mapDict = {}
    currentPatterns = []
    for line in lines[2:]:
        split = line.split(' = ')
        mapDict[split[0]] = split[1].replace('(','').replace(')', '').strip().split(', ')
        if split[0][2] == 'A':
            currentPatterns.append(split[0])
    endingInZ = 0
    allLengths= []
    for node in currentPatterns:
        counter = 0
        while node[2] != 'Z':
            direction = pattern[counter % len(pattern)]
            if direction == 'L':
                node = (mapDict[node][0])
            else:
                node = (mapDict[node][1])
            counter += 1
        allLengths.append(counter)
    lcm = math.lcm(*allLengths)
    print(lcm)