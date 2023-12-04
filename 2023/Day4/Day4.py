import re

# Part 1

f = open("input.txt", "r")
# f = open("testdata.txt", "r")
inputData = f.readlines()
totalpoints = 0

def getPoints(scratchCard):
    cardpoints = 0
    numbers = scratchCard.split(':')[1].split('|')
    winningNumbers = numbers[0].split()
    lottoNumbers = numbers[1].split()
    for x in winningNumbers:
        for y in lottoNumbers:
            if x == y:
                if cardpoints == 0:
                    cardpoints = 1
                else:
                    cardpoints *= 2
    return cardpoints

def getCopies(scratchCard):
    cardpoints = 0
    numbers = scratchCard.split(':')[1].split('|')
    winningNumbers = numbers[0].split()
    lottoNumbers = numbers[1].split()
    for x in winningNumbers:
        for y in lottoNumbers:
            if x == y:
                cardpoints += 1
    return cardpoints

# Part 1

for x in inputData:
    totalpoints += getPoints(x)
print(totalpoints)

# Part 2
cardAmount = list()
for i in range(len(inputData)):
    cardAmount.append(1)

for i, x in enumerate(inputData):
    print("Running card " + str(i) + " for " + str(cardAmount[i]) + " times")
    for j in range(cardAmount[i]):
        for k in range(getCopies(x)):
            try:
                cardAmount[i+k+1] += 1
            except:
                1+1
print(sum(cardAmount))

