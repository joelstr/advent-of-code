import math

# Part 1

f = open("2023/Day7/input.txt", "r")
# f = open("2023/Day7/testdata.txt", "r")
inputData = f.readlines()

cardValues=['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

cards = list()

def getHandType(hand):
    sets = list()
    for card in set(hand):
        sets.append(hand.count(card))
    
    if max(sets) == 5:
        return 7
    elif max(sets) == 4:
        return 6
    elif max(sets) == 3:
        if 2 in sets:
            return 5
        else:
            return 4
    elif max(sets) == 2:
        if sets.count(2) == 2:
            return 3
        else:
            return 2
    else:
        return 1
    
def getHandTypeWithJ(hand):
    sets = list()
    nofJ = hand.count('J')
    for card in set(hand):
        if card != 'J':
            sets.append(hand.count(card))
    if nofJ == 5:
        return 7
    if max(sets)+nofJ == 5:
        return 7
    elif max(sets)+nofJ == 4:
        return 6
    elif max(sets)+nofJ == 3:
        if nofJ == 1:
            if sets.count(2) == 2:
                return 5
            else:
                return 4
        else:
            if 2 in sets:
                return 5
            else:
                return 4
    elif max(sets)+nofJ == 2:
        if sets.count(2) == 2:
            return 3
        else:
            return 2
    else:
        return 1
    
def getBetter(card1, card2):
    for idx, x in enumerate(card1[0]):
        if cardValues.index(x) < cardValues.index(card2[0][idx]):
            return True
        elif cardValues.index(x) > cardValues.index(card2[0][idx]):
            return False
    return False

for x in inputData:
    tmp = [x.split()[0], int(x.split()[1])]
    tmp.append(getHandType(tmp[0]))
    cards.append(tmp)

cards.sort(key = lambda x: x[2])

l = len(cards)
for j in range(0,l):
    for i in range(len(cards)-1- j):
        if cards[i][2] == cards[i+1][2]:
            if getBetter(cards[i], cards[i+1]):
                tmp = cards[i+1]
                cards[i+1] = cards[i]
                cards[i] = tmp

winnings = 0
for idx, x in enumerate(cards):
    winnings += (idx+1) * x[1]

# print(cards)
print(winnings)




# Part 2

cards.clear()

for x in inputData:
    tmp = [x.split()[0], int(x.split()[1])]
    tmp.append(getHandTypeWithJ(tmp[0]))
    cards.append(tmp)

cards.sort(key = lambda x: x[2])

l = len(cards)
for j in range(0,l):
    for i in range(len(cards)-1- j):
        if cards[i][2] == cards[i+1][2]:
            if getBetter(cards[i], cards[i+1]):
                tmp = cards[i+1]
                cards[i+1] = cards[i]
                cards[i] = tmp

winnings = 0
for idx, x in enumerate(cards):
    winnings += (idx+1) * x[1]

print(winnings)