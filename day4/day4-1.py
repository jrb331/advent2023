with open("input.txt", "r") as f:
    lines = f.readlines()

totalWinningNumbers = 0
for line in lines:
    winningNumbers = list(filter(None, line.split(':')[1].split('|')[0].strip().split(" ")))
    myNumbers = list(filter(None,line.split(':')[1].split('|')[1].strip().split(" ")))
    myWinningNumbers = 0
    for number in myNumbers:
        if number in winningNumbers:
            myWinningNumbers+=1
    if myWinningNumbers != 0:
        myWinningNumbers = pow(2, myWinningNumbers-1)
    totalWinningNumbers += myWinningNumbers
print(totalWinningNumbers)