with open("input.txt", "r") as f:
    lines = f.readlines()

time = lines[0].split(':')
time = int(time[1].strip().replace(' ', ''))
distance = lines[1].split(':')
distance = int(distance[1].strip().replace(' ', ''))
winningCount = 0
for buttonHoldTime in range(0,time+1):
    remainingTime = time - buttonHoldTime
    newDistance = buttonHoldTime*remainingTime
    if newDistance > distance:
        winningCount+=1
print(winningCount)
