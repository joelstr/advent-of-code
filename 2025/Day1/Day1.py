import numpy as np


# Part 1

# f = open("2025/Day1/input.txt", "r")
f = open("2025/Day1/testdata.txt", "r")
inputData = f.readlines()

currentPos = 50
zeros = 0
for x in inputData:
    if x[0] == "L":
        currentPos -= int(x[1:])
    elif x[0] == "R":
        currentPos += int(x[1:])
    while currentPos > 99:
        currentPos -= 100
    while currentPos < 0:
        currentPos += 100
    if currentPos == 0:
        zeros += 1

print("Number of zeros: " + str(zeros))
    
# Part 2

currentPos = 50
zeros = 0
for x in inputData:
    if x[0] == "L":
        for _ in range(int(x[1:])):
            currentPos -= 1
            if currentPos < 0:
                currentPos += 100
            if currentPos == 0:
                zeros += 1
    elif x[0] == "R":
        for _ in range(int(x[1:])):
            currentPos += 1
            if currentPos > 99:
                currentPos -= 100
            if currentPos == 0:
                zeros += 1
    print("Current pos: " + str(currentPos))

print("Number of zeros: " + str(zeros))