import os
import numpy as np

filename = os.path.dirname(__file__) + "\\input.txt"
f = open(filename, "r")
inputData = f.readlines()

fish = np.zeros((9,1))

for x in inputData[0].strip().split(','):
    fish[int(x)] += 1

for i in range(256):
    tmpfish = fish[0]
    fish = np.roll(fish,-1)
    fish[6] += tmpfish


print(int(sum(fish)))