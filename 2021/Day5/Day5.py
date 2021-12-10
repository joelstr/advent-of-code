import os
import numpy as np

filename = os.path.dirname(__file__) + "\\input.txt"
f = open(filename, "r")
inputData = f.readlines()

oceanfloor = np.zeros([1000, 1000],dtype=int)

def addlines(data):
    global oceanfloor
    flip = False
    xy1, xy2 = data.split(' -> ')
    x1, y1 = [int(x) for x in xy1.strip().split(',')]
    x2, y2 = [int(y) for y in xy2.strip().split(',')]
    if x2 < x1:
        flip = not flip
        x1, x2 = x2, x1
    if y2 < y1:
        flip = not flip
        y1, y2 = y2, y1
    x2 += 1
    y2 += 1
    if x1 == x2-1:
        oceanfloor[y1:y2,x1:x2] += 1
    elif y1 == y2-1:
        oceanfloor[y1:y2,x1:x2] += 1
    else:
        tmp = np.zeros((y2-y1,x2-x1),int)
        np.fill_diagonal(tmp,1)
        if flip:
            tmp = np.flipud(tmp)
        oceanfloor[y1:y2,x1:x2] += tmp
        # print(oceanfloor)

for line in inputData:
    addlines(line)
# x1 = 0
# x2 = 6
# y1 = 9
# y2 = 10
# oceanfloor[y1:y2,x1:x2] += 1
# print(oceanfloor)
# print(oceanfloor[oceanfloor>1])
# print(np.size(oceanfloor))
print(len(oceanfloor[oceanfloor>1]))