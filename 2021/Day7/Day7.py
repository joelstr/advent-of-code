import os
import numpy as np
import math

filename = os.path.dirname(__file__) + "\\input.txt"
f = open(filename, "r")
inputData = f.readlines()

crabs = np.array(inputData[0].strip().split(','),int)
median = np.median(crabs)

print(sum(np.abs(crabs - median)))

# Part 2

mean = math.floor(np.mean(crabs))
print(np.mean(crabs))
fuel = 0
for x in np.abs(crabs - mean):
    fuel += sum(range(1,x+1))

print(fuel)
