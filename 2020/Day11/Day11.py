import numpy as np
import copy

# f = open("Day11/input.txt", "r")
f = open("Day11/test.txt", "r")
# f = open("Day11/smalltest.txt", "r")
inputData = f.read().splitlines()
# inputData = list(map(int,inputData))
grid = []
for l in inputData:
    grid.append(list(l))
gridChange = True

# print(grid)
tmpGrid = copy.deepcopy(grid)

while gridChange:
    gridChange = False
    for i in range(0,len(inputData)):
        for j in range(0,len(inputData[0])):
            neighbours = 0
            if grid[i][j] == 'L':
                try:
                    neighbours += grid[i-1][j-1:j+1].count('#')
                    neighbours += grid[i][j-1:j+1].count('#')
                    neighbours += grid[i+1][j-1:j+1].count('#')
                except:
                    neighbours += 0
                if neighbours == 0:
                    tmpGrid[i][j] = '#'
                    gridChange = True
            elif grid[i][j] == '#':
                try:
                    neighbours += grid[i-1][j-1:j+1].count('#')
                    neighbours += grid[i][j-1:j+1].count('#')
                    neighbours += grid[i+1][j-1:j+1].count('#')
                except:
                    neighbours += 0
                if neighbours >= 4:
                    tmpGrid[i][j] = 'L'
                    gridChange = True
    grid = copy.deepcopy(tmpGrid)

print(grid.count('#'))