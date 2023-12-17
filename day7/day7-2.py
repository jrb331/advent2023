def testFunc(e):
    return e[3][0]

with open("input.txt", "r") as f:
    lines = f.readlines()

cardToInt = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    'J': 1
}

cardData=[]
handTypes=[]
for i in range(7):
    handTypes.append([])
for line in lines:
    line = line.strip().split(' ')
    cardData.append([line[0], int(line[1])])
for idx, data in enumerate(cardData):
    cardDict = {}
    noChars = []
    for card in data[0]:
        if card in cardDict:
            cardDict[card]+=1
        else:
            cardDict[card]=1
        if card in cardToInt.keys():
            noChars.append(cardToInt[card])
        else:
            noChars.append(int(card))
    cardData[idx].append(cardDict)
    cardData[idx].append(noChars)
for hand in cardData:
    cardDict = hand[2]
    jokers = 0
    if 'J' in cardDict.keys():
        jokers = cardDict['J']
    # five of kind
    if len(cardDict.keys())==1:
        handTypes[0].append(hand)
    elif len(cardDict.keys())==2:
        # four of kind
        if any(value >= 4 for value in cardDict.values()):
            if jokers > 0:
                handTypes[0].append(hand)
            else:
                handTypes[1].append(hand)
        # full house
        else:
            if jokers > 0:
                handTypes[0].append(hand)
            else:
                handTypes[2].append(hand)
    elif len(cardDict.keys())==3:
        #three of kind
        if any(value >= 3 for value in cardDict.values()):
            if jokers > 0:
                handTypes[1].append(hand)
            else:
                handTypes[3].append(hand)
        #two pair
        else:
            if jokers > 0:
                if jokers >= 2:
                    handTypes[1].append(hand)
                else:
                    handTypes[2].append(hand)
            else:
                handTypes[4].append(hand)
    # one pair
    elif len(cardDict.keys())==4:
        if jokers > 0:
            handTypes[3].append(hand)
        else:
            handTypes[5].append(hand)
    # high card
    else:
        if jokers > 0:
            handTypes[5].append(hand)
        else:
            handTypes[6].append(hand)


for idx, handType in enumerate(handTypes):
    handTypes[idx] = sorted(handType, key=lambda x: tuple(x[-1]), reverse=True)
sortedHands=[]
for handType in handTypes:
    for hand in handType:
        sortedHands.append(hand)
count = 0
for idx, hand in enumerate(sortedHands):
    count+=(hand[1]*(len(sortedHands)-idx))
print(count)

