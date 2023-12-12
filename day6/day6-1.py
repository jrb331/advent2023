with open("input.txt", "r") as f:
    lines = f.readlines()

times = lines[0].split(':')
distances = lines[1].split(':')
times = list(int(x) for x in (filter(None, times[1].strip().split(' '))))
distances = list(int(x) for x in (filter(None, distances[1].strip().split(' '))))
timeDistancePairs = []
for idx in range(0,len(times)):
    timeDistancePairs.append([times[idx], distances[idx]])
winningTimes = []
winningProduct = 1
for pair in timeDistancePairs:
    winningCount = 0
    for buttonHoldTime in range(0,pair[0]+1):
        remainingTime = pair[0] - buttonHoldTime
        distance = buttonHoldTime*remainingTime
        if distance > pair[1]:
            winningCount+=1
    winningTimes.append(winningCount)
for time in winningTimes:
    winningProduct*=time
print(winningProduct)