import numpy as np

# Part 1

f = open("2024/Day1/input.txt", "r")
# f = open("2024/Day1/testdata.txt", "r")
inputData = f.readlines()

list1 = []
list2 = []

for x in inputData:
    y = x.split()
    list1.append(int(y[0]))
    list2.append(int(y[1]))

list1.sort()
list2.sort()
list1 = np.array(list1)
list2 = np.array(list2)

diff = np.subtract(list1, list2)
print(sum(abs(diff)))

#Part 2
simVal = 0
for x in list1:
    simVal += (list2 == x).sum()*x

print(simVal)