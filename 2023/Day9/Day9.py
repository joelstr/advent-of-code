import time
import numpy as np

f = open("2023/Day9/input.txt", "r")
# f = open("2023/Day9/testdata.txt", "r")
inputData = f.readlines()

start_time = time.time()

def Part1():
    totalValue = 0
    for x in inputData:
        seq = np.array(list(map(int,x.split())))
        lastValue = list()
        lastValue.append(seq[-1])
        while seq.any():
            seq = seq[1:]-seq[0:-1]
            lastValue.append(seq[-1])
        totalValue += sum(lastValue)
    print(totalValue)

def Part2():
    totalValue = 0
    for x in inputData:
        seq = np.array(list(map(int,x.split())))
        lastValue = list()
        lastValue.append(seq[0])
        while seq.any():
            seq = seq[1:]-seq[0:-1]
            lastValue.append(seq[0])
        mem = 0
        for idx in reversed(range(0,len(lastValue)-1)):
            mem = lastValue[idx] - mem

        totalValue += mem
    print(totalValue)

if __name__ == '__main__':
    try:
        Part1()
    except KeyboardInterrupt:
       print("Run interrupted during part 1 after %s seconds" % (time.time() - start_time))

    try:
        Part2()
    except KeyboardInterrupt:
       print("Run interrupted during part 1 after %s seconds" % (time.time() - start_time))


    print("Runtime %s seconds" % (time.time() - start_time))