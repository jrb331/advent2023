from itertools import product

with open("sample.txt", "r") as f:
    lines = f.read().strip().split('\n')

springList = []
damagedSprings = []
for line in lines:
    data = line.split(' ')
    springList.append(data[0])
    damagedSprings.append(list(map(int, data[1].split(","))))


print(springList)
print(damagedSprings)


def combos(springs, target):
    line = []
    idxs = []
    for idx, char in enumerate(springs):
        if char == '.':
            line.append(0)
        elif char == '?':
            line.append(-1)
            idxs.append(idx)
        elif char == '#':
            line.append(1)
    
    for combination in product([0, 1], repeat=len(idxs)):
        lineCopy = line.copy()
        for i, value in zip(idxs, combination):
           lineCopy[i] = value
           
        print(lineCopy)

count = 0
for springs, target in list(zip(springList, damagedSprings)):
    res = combos(springs, target)
    count += res

# for line in allLocations:
    
'''
find the lengths and locations of the ? groups
find the lengths and locations of the # groups
for each number, find the positions in the string that would still 
leave enough room for the rest of the numbers


'''