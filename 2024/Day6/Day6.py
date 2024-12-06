import numpy as np
import re

# Part 1

f = open("2024/Day6/input.txt", "r")
# f = open("2024/Day6/testdata.txt", "r")
inputData = f.readlines()
inputData = [x.strip() for x in inputData]
for i, data in enumerate(inputData):
    inputData[i] = list(data)
    if '^' in data:
        pos = (i, data.index('^'))
        startPos = pos
        firstPos = pos

direction = 'U'

def move(pos, direction):
    if direction == 'U':
        if inputData[pos[0]-1][pos[1]] == '#':
            direction = 'R'
            return move(pos, direction)
        else:
            return (pos[0]-1, pos[1]), direction
    elif direction == 'R':
        if inputData[pos[0]][pos[1]+1] == '#':
            direction = 'D'
            return move(pos, direction)
        else:
            return (pos[0], pos[1]+1), direction
    elif direction == 'D':
        if inputData[pos[0]+1][pos[1]] == '#':
            direction = 'L'
            return move(pos, direction)
        else:
            return (pos[0]+1, pos[1]), direction
    elif direction == 'L':
        if inputData[pos[0]][pos[1]-1] == '#':
            direction = 'U'
            return move(pos, direction)
        else:
            return (pos[0], pos[1]-1), direction
        
def extendTrack(pos, direction):
    if direction == 'U':
        if inputData[pos[0]][pos[1]-1] == '#':
            return (pos[0], pos[1]-1), direction
        else:
            return (pos[0], pos[1]-1), direction
    elif direction == 'R':
        if inputData[pos[0]-1][pos[1]] == '#':
            return (pos[0]-1, pos[1]), direction
        else:
            return (pos[0]-1, pos[1]), direction
    elif direction == 'D':
        if inputData[pos[0]][pos[1]+1] == '#':
            return (pos[0], pos[1]+1), direction
        else:
            return (pos[0], pos[1]+1), direction
    elif direction == 'L':
        if inputData[pos[0]+1][pos[1]] == '#':
            return (pos[0]+1, pos[1]), direction
        else:
            return (pos[0]+1, pos[1]), direction
        
inMap = True
passedPositions = []
while inMap:
    if (pos, direction) not in passedPositions:
        if pos[0] < 0:
            inMap = False
            break
        passedPositions.append((pos, direction))

    try:
        pos, direction = move(pos, direction)
            
    except IndexError:
        inMap = False

# visitedPositions = 0
# for x in inputData:
#     visitedPositions += x.count('X')
#     print("".join(x))
uniquePositions = []
for x in passedPositions:
    if x[0] not in uniquePositions:
        uniquePositions.append(x[0])
print(len(uniquePositions))

#Part 2

guardTrack = []
uniquePositions = []
while startPos[0]+1 < len(inputData) and inputData[startPos[0]+1][startPos[1]] != '#':
    startPos = (startPos[0]+1, startPos[1])
    passedPositions.append((startPos, 'U'))

prevTurn = passedPositions[0]
for x in passedPositions:
    if x[1] != prevTurn[1]:
        currentPos = x[0]
        if x[1] == 'U':
            while currentPos[0]+1 < len(inputData) and inputData[currentPos[0]+1][currentPos[1]] != '#':
                currentPos = (currentPos[0]+1, currentPos[1])
                passedPositions.append((currentPos, 'U'))
        if x[1] == 'D':
            while currentPos[0]-1 >= 0 and inputData[currentPos[0]-1][currentPos[1]] != '#':
                currentPos = (currentPos[0]-1, currentPos[1])
                passedPositions.append((currentPos, 'D'))
        if x[1] == 'R':
            while currentPos[1]-1 >= 0 and inputData[currentPos[0]][currentPos[1]-1] != '#':
                currentPos = (currentPos[0], currentPos[1]-1)
                passedPositions.append((currentPos, 'R'))
        if x[1] == 'L':
            while currentPos[1]+1 < len(inputData[0]) and inputData[currentPos[0]][currentPos[1]+1] != '#':
                currentPos = (currentPos[0], currentPos[1]+1)
                passedPositions.append((currentPos, 'L'))

possibleBlocks = []
for x in passedPositions:
    if x[0] in uniquePositions:
        for y in guardTrack:
            if y[0] == x[0]:
                if x[1] == 'U' and y[1] == 'R':
                    if (x[0][0]-1,x[0][1]) not in possibleBlocks and (x[0][0]-1,x[0][1]) != firstPos:
                        possibleBlocks.append((x[0][0]-1,x[0][1]))
                elif x[1] == 'R' and y[1] == 'D':
                    if (x[0][0],x[0][1]+1) not in possibleBlocks and (x[0][0],x[0][1]+1) != firstPos:
                        possibleBlocks.append((x[0][0],x[0][1]+1))
                elif x[1] == 'D' and y[1] == 'L':
                    if (x[0][0]+1,x[0][1]) not in possibleBlocks and (x[0][0]+1,x[0][1]) != firstPos:
                        possibleBlocks.append((x[0][0]+1,x[0][1]))
                elif x[1] == 'L' and y[1] == 'U':
                    if (x[0][0],x[0][1]-1) not in possibleBlocks and (x[0][0],x[0][1]-1) != firstPos:
                        possibleBlocks.append((x[0][0],x[0][1]-1))
    guardTrack.append(x)
    uniquePositions.append(x[0])

print(startPos)
print(possibleBlocks)
print(len(possibleBlocks))