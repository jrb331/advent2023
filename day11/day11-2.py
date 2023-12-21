from itertools import combinations

MULTIPLIER=1000000

with open("input.txt", "r") as f:
    lines = f.readlines()

galaxies = []
emptyRows = []
emptyColumns = {}
# print(len(lines))
for yidx, line in enumerate(lines):
    line = line.strip()
    if '#' not in line:
        emptyRows.append(yidx)
    for xidx, char in enumerate(line):
        if char == '.':
            if xidx not in emptyColumns.keys():
                emptyColumns[xidx] = 1
            else:
                emptyColumns[xidx]+=1
        elif char == '#':
            galaxies.append((xidx, yidx))
# print(emptyColumns)
for key in list(emptyColumns):
    if emptyColumns[key] < len(lines):
        # print(f"{emptyColumns[key]} is less than {len(lines)} so I'm removing {key} from the dict")
        emptyColumns.pop(key)
# print(f"empty rows: {emptyRows}")
# print(f"empty columns: {emptyColumns.keys()}")
# print(f"galaxy locations: {galaxies}")
extendedLocations = []
for galaxy in galaxies:
    # print(f"galaxy: {galaxy}")
    newX = 0
    newY = 0
    columnsCrossed = 0
    rowsCrossed = 0
    for emptyRow in emptyRows:
        if emptyRow < galaxy[1]:
            rowsCrossed+=1
    for emptyColumn in emptyColumns.keys():
        if emptyColumn < galaxy[0]:
            columnsCrossed+=1
    # print(f"rows crossed: {rowsCrossed}")
    # print(f"columns crossed: {columnsCrossed}")
    newX = galaxy[0] + (MULTIPLIER-1)*columnsCrossed
    newY = galaxy[1] + (MULTIPLIER-1)*rowsCrossed
    extendedLocations.append((newX, newY))
# print(f"extended locays:  {extendedLocations}")

combos = [combo for combo in combinations(extendedLocations, 2)]
dists = 0
for combo in combos:
    dists +=abs(combo[0][0] - combo[1][0]) + abs(combo[0][1]-combo[1][1])
print(dists)
