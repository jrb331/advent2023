import re
PATTERN = r'^[.\d]+$'
PATTERN2 = r'\d'
with open("input.txt", "r") as f:
    lines = f.readlines()

sum = 0
# for lineIndex, currentLine in enumerate(lines):
#     currentLine = ''.join(currentLine)
#     digitStart = None
#     digitEnd = None

#     if lineIndex == 0:
#         prevLine = currentLine
#     if lineIndex >= len(lines)-1:
#         nextLine = currentLine
#     else:
#         nextLine = lines[lineIndex+1]

#     for charIndex, char in enumerate(currentLine):
#         print(digitStart)
#         print(digitEnd)
#         if char.isdigit() and digitStart is None:
#             digitStart = charIndex
#             digitEnd = charIndex
#         elif char.isdigit() and digitStart is not None:
#             digitEnd = charIndex
#         elif not char.isdigit() and digitStart is not None:
#             if digitStart > 0:
#                 digitFinder = digitStart - 1
#             else:
#                 digitFinder = 0
#             if  not bool(re.match(PATTERN, currentLine[digitFinder:digitEnd+2])) or \
#                 not bool(re.match(PATTERN, prevLine[digitFinder:digitEnd+2])) or \
#                 not bool(re.match(PATTERN, nextLine[digitFinder:digitEnd+2])):
#                     wholeNumber = ''.join(currentLine[digitStart:digitEnd+1])
#                     print(wholeNumber)
#                     sum += int(wholeNumber)
#             digitStart = None
#             digitEnd = None

#     prevLine = currentLine
# print(sum)

def searchForward(line, startIndex):
    entireNumber = ''
    for char in line[startIndex:]:
        if char.isdigit():
            entireNumber += char
        else:
            break
    return entireNumber
def searchBackward(line, endIndex):
    reversedLine = line[::-1]
    reversedEntireNumber = ''
    #need to verify these indexes will always work
    for char in reversedLine[len(line)-endIndex-1:]:
        if char.isdigit():
            reversedEntireNumber += char
        else:
            break
    return reversedEntireNumber[::-1]


for lineIndex, currentLine in enumerate(lines):
    currentLine = currentLine.strip()
    
    if lineIndex == 0:
        prevLine = currentLine
    if lineIndex >= len(lines)-1:
        nextLine = currentLine
    else:
        nextLine = lines[lineIndex+1]

    for charIndex, char in enumerate(currentLine):
        adjacentNumbersCount = 0
        if char == '*':
            if charIndex == 0:
                searchSpanStart = 0
            else:
                searchSpanStart = charIndex-1
            if charIndex == len(currentLine)-1:
                searchSpanEnd = charIndex
            else:
                searchSpanEnd = charIndex + 1
            if currentLine[searchSpanEnd].isdigit():
                adjacentNumbersCount += 1
            if currentLine[searchSpanStart].isdigit():
                adjacentNumbersCount += 1
            if nextLine != currentLine:
                if nextLine[charIndex].isdigit():
                    adjacentNumbersCount += 1
                else:
                    matches = re.findall(PATTERN2, nextLine[searchSpanStart:searchSpanEnd+1])
                    adjacentNumbersCount += len(matches)
            if prevLine != currentLine: 
                if prevLine[charIndex].isdigit():
                    adjacentNumbersCount+=1
                else:
                    matches = re.findall(PATTERN2, prevLine[searchSpanStart:searchSpanEnd+1])
                    adjacentNumbersCount += len(matches)
        if adjacentNumbersCount < 2:
            continue
        adjacentNumbersList = []
        #search line below
        if nextLine != currentLine:
            if nextLine[charIndex].isdigit():
                frontHalf = searchForward(nextLine,charIndex)
                backHalf = searchBackward(nextLine, searchSpanStart)
                entireNumber = int(backHalf + frontHalf)
                adjacentNumbersList.append(entireNumber)
            elif re.findall(PATTERN2, nextLine[searchSpanStart:searchSpanEnd+1]):
                numberInFront = searchForward(nextLine, searchSpanEnd)
                numberBehind = searchBackward(nextLine, searchSpanStart)
                if numberBehind:
                    adjacentNumbersList.append(int(numberBehind))
                if numberInFront:
                    adjacentNumbersList.append(int(numberInFront))
        # search line above
        if prevLine != currentLine:
            if prevLine[charIndex].isdigit():
                frontHalf = searchForward(prevLine,charIndex)
                backHalf = searchBackward(prevLine, searchSpanStart)
                entireNumber = int(backHalf + frontHalf)
                adjacentNumbersList.append(entireNumber)
            elif re.findall(PATTERN2, prevLine[searchSpanStart:searchSpanEnd+1]):
                numberInFront = searchForward(prevLine, searchSpanEnd)
                numberBehind = searchBackward(prevLine, searchSpanStart)
                if numberBehind:
                    adjacentNumbersList.append(int(numberBehind))
                if numberInFront:
                    adjacentNumbersList.append(int(numberInFront))
        if currentLine[searchSpanEnd].isdigit():
            numberInFront = searchForward(currentLine, searchSpanEnd)
            adjacentNumbersList.append(int(numberInFront))
        if currentLine[searchSpanStart].isdigit():
            numberBehind = searchBackward(currentLine, searchSpanStart)
            adjacentNumbersList.append(int(numberBehind))
        gearRatio = 1
        for number in adjacentNumbersList:
            gearRatio *= number
        sum += gearRatio
    prevLine = currentLine
print(sum)