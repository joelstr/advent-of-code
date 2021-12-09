import os
from typing import overload
import numpy as np

filename = os.path.dirname(__file__) + "\\test.txt"
f = open(filename, "r")
inputData = f.readlines()

oceanfloor = np.zeros([10, 10],dtype=int)

def addlines(data):
    global oceanfloor
    xy1, xy2 = data.split(' -> ')
    x1, y1 = [int(x) for x in xy1.strip().split(',')]
    x2, y2 = [int(y) for y in xy2.strip().split(',')]
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1
    x2 += 1
    y2 += 1
    if x1 == x2-1:
        oceanfloor[y1:y2,x1:x2] += 1
    elif y1 == y2-1:
        oceanfloor[y1:y2,x1:x2] += 1

for line in inputData:
    addlines(line)
# x1 = 0
# x2 = 6
# y1 = 9
# y2 = 10
# oceanfloor[y1:y2,x1:x2] += 1
# print(oceanfloor)
print(oceanfloor[oceanfloor>1])
print(len(oceanfloor[oceanfloor>1]))