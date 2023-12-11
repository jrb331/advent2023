with open("input.txt", "r") as f:
    lines = f.readlines()

totalWinningNumbers = 0
cardDict = {}
for idx in range(len(lines)):
    cardDict[idx+1] = 1
for cardNumber, line in enumerate(lines):
    cardNumber+=1
    winningNumbers = list(filter(None, line.split(':')[1].split('|')[0].strip().split(" ")))
    myNumbers = list(filter(None,line.split(':')[1].split('|')[1].strip().split(" ")))
    myWinningNumbers =[]
    for number in myNumbers:
        if number in winningNumbers:
            myWinningNumbers.append(number)
    for idx in range(len(myWinningNumbers)):
        idx+=1
        cardDict[cardNumber+idx]+=cardDict[cardNumber]
for key in cardDict:
    totalWinningNumbers+=cardDict[key]
print(totalWinningNumbers)