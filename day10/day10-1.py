import math
test = {
    "left": ['-', 'F', 'L'],
    "right": ['-', 'J', '7'],
    "up": ['|', '7', 'F'],
    "down": ['|', 'L', 'J']
}

options = {
    '|': ['up', 'down'],
    '-': ['left', 'right'],
    '7': ['left', 'down'],
    'F': ['right', 'down'],
    'L': ['right', 'up'],
    'J': ['left', 'up']
}

opposite = {
    'up': 'down', 
    'down': 'up',
    'left': 'right',
    'right': 'left'
}

# def nextStep(grid, x, y, prev):
#     currChar = grid[y][x]
#     print(f"currently at position {x}, {y} at char {currChar}")
#     if currChar == 'S':
#         print("base case. loop complete")
#         return 0
#     # print(options[currChar])
#     # print(prev)
#     nextDir = options[currChar]
#     print(f"all options: {nextDir}")
#     print(prev)
#     if nextDir[0] == prev:
#         nextDir = nextDir[1]
#     else:
#         nextDir = nextDir[0]
#     # nextDir.remove(prev)
#     print(f"option after removal: {nextDir}")
#     # print(f"next Direction: {nextDir}")
#     print(f"next direction: {nextDir}")
#     print(f"since I came from {prev} and my current character is {currChar}, I must go {nextDir}")
#     if nextDir == 'up':
#         y-=1
#     elif nextDir == 'down':
#         y+=1
#     elif nextDir == 'right':
#         x+=1
#     else:
#         x-=1
#     return 1 + nextStep(grid, x, y, opposite[nextDir])

with open("input.txt", "r") as f:
    lines = f.readlines()

grid = []
x = 0
y = 0
for idx, line in enumerate(lines):
    line = line.strip()
    grid.append(line)
    if x == 0 & y == 0:
        for c, char in enumerate(line):
            if char == 'S':
                y = idx
                x = c
                
# print(f"{x}, {y}")
# print(grid)
# print(grid[y][x])
# print(grid[y+1][x]) # down
# print(grid[y-1][x]) # up
# print(grid[y][x+1]) # right
# print(grid[y][x-1]) # left
# opposite[nextDir]
nextList = []
if grid[y+1][x] in test['down']:
    nextList.append('down')
if grid[y-1][x] in test['up']:
    nextList.append('up')
if grid[y][x+1] in test['right']:
    nextList.append('right')
if grid[y][x-1] in test['left']:
    nextList.append('left')
print(nextList)


if nextList[0] == 'up':
    print("going up")
    y-=1
elif nextList[0] == 'down':
    print("going down")
    y+=1
elif nextList[0] == 'right':
    print("going right")
    x+=1
else:
    print("going left")
    x-=1

prev = opposite[nextList[0]]
print(prev)

print(f"{x}, {y}")
print(grid[y][x])
currChar = grid[y][x]
steps = 0
while currChar != 'S':
    print(f"currently at position {x}, {y} at char {currChar}")
    nextDir = options[currChar]
    if nextDir[0] == prev:
        nextDir = nextDir[1]
    else:
        nextDir = nextDir[0]
    print(f"since I came from {prev} and my current character is {currChar}, I must go {nextDir}")
    prev = opposite[nextDir]
    if nextDir == 'up':
        y-=1
    elif nextDir == 'down':
        y+=1
    elif nextDir == 'right':
        x+=1
    else:
        x-=1
    currChar=grid[y][x]
    steps+=1
steps = math.ceil(steps/2)
print(steps)


