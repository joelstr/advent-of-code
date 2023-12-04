import re

# Part 1

f = open("input.txt", "r")
# f = open("testdata.txt", "r")
inputData = f.readlines()
partNumbers = 0

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

for idx, x in enumerate(inputData):
    tmp = re.findall(r'\d+', x)
    indices = [m.start() for m in re.finditer(r'\d+', x)]
    for loc, y in enumerate(tmp):
        if partOfSchematic([idx, indices[loc]],len(y)):
            partNumbers += int(y)
print(partNumbers)

