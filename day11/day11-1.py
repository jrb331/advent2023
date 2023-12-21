from itertools import combinations

with open("input.txt", "r") as f:
    lines = f.readlines()

emptyRows = []
emptyColumns = {}
emptyLine = ''
originalHeight = len(lines)
originalWidth = len(lines[0].strip())
for idx, line in enumerate(lines):
    line = line.strip()
    # print(line)
    if '#' not in line:
        emptyRows.append(idx)
        if not emptyLine:
            emptyLine = line
    for x, c in enumerate(line):
        if c == '.':
            if x not in emptyColumns.keys():
                emptyColumns[x] = 1
            else:
                emptyColumns[x] += 1
# print(emptyRows)
# print(emptyColumns)
for row in emptyRows[::-1]:
    lines.insert(row, emptyLine)
# print(lines)
# print(len(lines))
# for line in lines:
#     line=line.strip()
extendedLines = []
for line in lines:
    line = line.strip()
    for idx, c in enumerate(reversed(line.strip())):
        revidx = originalWidth - idx - 1
        # print(f"revidx: {revidx}")
        # print(f"the number of empty spots in this column {emptyColumns[revidx]}")
        # print(c)
        if emptyColumns[revidx] == originalWidth:
            # print("extending the line")
            line = line[:revidx] + '.' + line[revidx:]
            # print(line)
    extendedLines.append(line)

coordinates=[]
for y, line in enumerate(extendedLines):
    # print(line)
    for x, c in enumerate(line):
        if c == '#':
            coordinates.append((x,y))
print(coordinates)

combos = [combo for combo in combinations(coordinates, 2)]
# print(len(combos))
# print(combos[29])
dists = 0
test = combos[29]
for combo in combos:
    dists +=abs(combo[0][0] - combo[1][0]) + abs(combo[0][1]-combo[1][1])
print(dists)
