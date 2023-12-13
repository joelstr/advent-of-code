import time
import numpy as np
import re
start_time = time.time()

f = open("2023/Day13/input.txt", "r")
# f = open("2023/Day13/testdata.txt", "r")
inputData = f.read()
inputData = inputData.split('\n\n')

def FindRow(area):
    row = 0
    for idx in range(len(area)-1):
        rowFound = True
        for i in range(len(area)-idx):
            if idx - i < 0 or idx+i+1 >= len(area):
                break
            if not np.array_equal(area[idx-i],area[idx+i+1]):
                rowFound = False
                break
        if rowFound:
            row = idx+1
            break
    return row

def Part1():
    totalValue = 0
    for x in inputData:
        area = np.array([list(y) for y in x.split('\n')])
        totalValue += FindRow(area) * 100 + FindRow(area.T)
    print(totalValue)
        


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