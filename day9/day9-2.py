def getDiffs(line):
    diffs = []
    if all(num == 0 for num in line):
        return 0
    for idx in range(len(line)):
        if idx + 1 < len(line):
            diffs.append(line[idx+1] - line[idx])
        else:
            return line[0] - getDiffs(diffs)

with open("input.txt", "r") as f:
    lines = f.readlines()
predictions = []
for line in lines:
    line = list(int(x) for x in line.strip().split(' '))
    predictions.append(getDiffs(line))
print(sum(predictions))