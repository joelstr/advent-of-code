import time
import numpy as np
start_time = time.time()

f = open("2023/Day11/input.txt", "r")
# f = open("2023/Day11/testdata.txt", "r")
inputData = f.readlines()

galaxies = [list(sub.strip()) for sub in inputData]
galaxies = np.array(galaxies)

emptyRows = list()

for idx, x in enumerate(galaxies):
    if '#' not in x:
        emptyRows.append(idx)

# for x in reversed(emptyRows):
#     galaxies = np.insert(galaxies, x, '.', axis = 0)
    

emptyCols = list()

for idx, x in enumerate(galaxies.T):
    if '#' not in x:
        emptyCols.append(idx)

# for x in reversed(emptyCols):
#     galaxies = np.insert(galaxies, x, '.', axis = 1)



def Part1():
    coords = np.where(galaxies == '#')
    totalDistance = 0
    totalDistancePt2 = 0
    for i in range(len(coords[0])):
        for j in range(i+1,len(coords[0])):
            totalDistance +=  int(np.abs(coords[0][j] - coords[0][i]) + np.abs(coords[1][j]-coords[1][i]))
            totalDistancePt2 +=  int(np.abs(coords[0][j] - coords[0][i]) + np.abs(coords[1][j]-coords[1][i]))

            direction = 1
            if coords[0][i] > coords[0][j]:
                direction = -1
            for x in range(coords[0][i],coords[0][j],direction):
                if x in emptyRows:
                    totalDistance += 1
                    totalDistancePt2 += 999999

            direction = 1
            if coords[1][i] > coords[1][j]:
                direction = -1
            for x in range(coords[1][i],coords[1][j], direction):
                if x in emptyCols:
                    totalDistance += 1
                    totalDistancePt2 += 999999
    print(totalDistance) 
    print(totalDistancePt2) 
                


def Part2():
    pass

if __name__ == '__main__':
    try:
        Part1()
    except KeyboardInterrupt:
       print("Run interrupted during part 1 after %s seconds" % (time.time() - start_time))

    try:
        Part2()
    except KeyboardInterrupt:
       print("Run interrupted during part 2 after %s seconds" % (time.time() - start_time))


    print("Runtime %s seconds" % (time.time() - start_time))