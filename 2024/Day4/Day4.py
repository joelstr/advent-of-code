import numpy as np


# Part 1

f = open("2024/Day4/input.txt", "r")
# f = open("2024/Day4/testdata.txt", "r")
inputData = f.readlines()

data = []

for x in inputData:
    x = x.strip()
    data.append(list(x))

XMAS = 0
wordJumble = np.array(data)
for i in range(4):
    for x in wordJumble:
        XMAS += "".join(x).count("XMAS")
    for i in range(-len(wordJumble[0]), len(wordJumble[0])):
        XMAS += "".join(wordJumble.diagonal(i)).count("XMAS")
    wordJumble = np.rot90(wordJumble)

print(XMAS)
#Part 2

XMAS = 0
for i in range(1,len(data)-1):
    for j in range (1,len(data[0])-1):
        if data[i][j] == "A":
            if (data[i-1][j-1] == "M" and data[i+1][j+1] == "S") or (data[i-1][j-1] == "S" and data[i+1][j+1] == "M"):
                if (data[i-1][j+1] == "M" and data[i+1][j-1] == "S") or (data[i-1][j+1] == "S" and data[i+1][j-1] == "M"):
                    XMAS += 1

print(XMAS)