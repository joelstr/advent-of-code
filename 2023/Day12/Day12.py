import time
import numpy as np
import re
start_time = time.time()

# f = open("2023/Day12/input.txt", "r")
f = open("2023/Day12/testdata.txt", "r")
inputData = f.readlines()


def Part1():
    for x in inputData:
        springs, records = x.split()
        springs = list(springs)
        records = list(map(int,records.split(',')))

        print(springs)
        possibleString = list()
        for i in records:
            for j in range(i):
                possibleString.append('#')
            possibleString.append('.')
        possibleString = possibleString[0:-1]
        # print(possibleString)

        possible = True
        possibleStrings = list()
        possibleStrings.append(possibleString)
        records.append(0)
        # possibleString.insert(len(possibleString)-records[-1],'.')
        tmp = list()
        index = -1
        for i in reversed(records):
            index += i+1
            tmp = possibleString.copy()
            while len(tmp) < len(springs):
                tmp.insert(len(tmp)-index,'.')
                possibleStrings.append(tmp.copy())

        for s in possibleStrings:
            print(s)
        for idx, y in enumerate(possibleString):
            if x[idx] != '?' and y != x[idx]:
                possible = False
        print(possible)


        # questionmarks = np.where(springs == '?')
        # hashtags = np.where(springs == '#')
        # total = np.append(questionmarks,hashtags)
        # total = np.sort(total)
        # maxFollow = 0
        # tmp = 1
        # for i in range(len(total)-1):
        #     if total[i+1] == total[i]+1:
        #         tmp += 1
        #     else:
        #         tmp = 1
        #     if tmp > maxFollow:
        #         maxFollow = tmp
        
        # print(maxFollow)
        print(records)
        print(len(springs))
        print(sum(records)+len(records)-1)


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