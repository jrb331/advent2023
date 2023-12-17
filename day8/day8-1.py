with open("input.txt", "r") as f:
    lines = f.readlines()
    pattern = list(lines[0].strip())
    mapDict = {}
    for line in lines[2:]:
        split = line.split(' = ')
        mapDict[split[0]] = split[1].replace('(','').replace(')', '').strip().split(', ')
    currentPattern = 'AAA'
    counter = 0
    while currentPattern != 'ZZZ':
        direction = pattern[counter % len(pattern)]
        if direction == 'L':
            currentPattern = mapDict[currentPattern][0]
        else:
            currentPattern = mapDict[currentPattern][1]
        counter+=1
    print(counter)