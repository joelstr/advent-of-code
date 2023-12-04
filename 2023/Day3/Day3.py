import re

# Part 1

f = open("input.txt", "r")
# f = open("testdata.txt", "r")
inputData = f.readlines()
partNumbers = 0

cogCoords = list()
valueList = list()

def partOfSchematic(position, size):
    row = position[0] - 1
    col = position[1] - 1
    for i in range(row,row+3):
        if i >= 0 and i < len(inputData):
            for j in range(col,col+size+2):               
                if j >= 0 and j < len(inputData[0]) - 1:
                    if not inputData[i][j].isdigit() and inputData[i][j] != '.':
                        return True
    return False

def touchesCog(position, size, value):
    row = position[0] - 1
    col = position[1] - 1
    for i in range(row,row+3):
        if i >= 0 and i < len(inputData):
            for j in range(col,col+size+2):               
                if j >= 0 and j < len(inputData[0]) - 1:
                    if inputData[i][j] == '*':
                        cogCoords.append(str(i)+','+str(j))
                        valueList.append(value)

for idx, x in enumerate(inputData):
    tmp = re.findall(r'\d+', x)
    indices = [m.start() for m in re.finditer(r'\d+', x)]
    for loc, y in enumerate(tmp):
        if partOfSchematic([idx, indices[loc]],len(y)):
            partNumbers += int(y)
print(partNumbers)

for idx, x in enumerate(inputData):
    tmp = re.findall(r'\d+', x)
    indices = [m.start() for m in re.finditer(r'\d+', x)]
    for loc, y in enumerate(tmp):
        touchesCog([idx, indices[loc]],len(y),y)
totalGears = 0
for coord in cogCoords:
    occurences = [i for i, x in enumerate(cogCoords) if x == coord]
    if (len(occurences) == 2):
        totalGears += int(valueList[occurences[0]])*int(valueList[occurences[1]])

print(totalGears/2)
