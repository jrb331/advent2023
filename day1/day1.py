with open("text", "r") as f:
    lines = f.readlines()
count = 0
total = 0
numbersSpelled = ["one", "two", "three", "four", "five",
"six", "seven", "eight", "nine"]
wordMap = {k:v for (k,v) in zip(numbersSpelled, range(1,10))}
print(wordMap)
newLines = []
for line in lines:
    newline = ""
    for startIndex in range(len(line) -1):
        for endIndex in range(startIndex, len(line)):
            substr = line[startIndex:endIndex]
            print(substr)
            if substr in numbersSpelled:
                print(f"adding, {substr}")
                newline += str((wordMap[substr]))
            elif len(substr) == 1:
                try:
                    num = int(substr)
                    newline+=substr
                except:
                    continue

    newLines.append(newline)
    print(newline)
print(newLines);

for line in newLines:
    nums= []
    for char in line:
        try:
            number = int(char)
            print(f"adding {number}")
            nums.append(number)
        except ValueError:
            print(f"skipping {char}")
            continue
    print(nums)
    char1 = str(nums[0])
    char2 = str(nums[-1])
    total = int(char1 + char2)
    print(total)
    count += total
print(count)