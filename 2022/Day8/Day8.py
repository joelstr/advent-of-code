import numpy as np

# Part 1

f = open("input.txt", "r")
inputData = f.readlines()

visible = len(inputData)*2 + len(inputData[0].strip()*2) - 4

trees = []

for x in inputData[0:10]:
    row = list(map(int, x.strip()))
    trees.append(row)

trees = np.matrix(trees)

print(trees.shape)

# for i in range(1,98):
#     for j in range(1,98):
#         tree = trees[i,j]
#         print(tree)


# print(trees)
