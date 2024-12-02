import numpy as np

# Part 1

f = open("2024/Day2/input.txt", "r")
# f = open("2024/Day2/testdata.txt", "r")
inputData = f.readlines()



def evaluateReport(y):
    for x in range(len(y)-1):
        if y[x] - y[x+1] < 1 or y[x] - y[x+1] > 3:
            return False
    return True

# Part 1
safe = 0
for x in inputData:
    safeReport = True
    y = [int(n) for n in x.split()]
    if y[0] < y[1]:
        y.reverse()

    if (evaluateReport(y)):
        safe += 1



print(safe)

#Part 2
safe = 0
for x in inputData:
    safeReport = True
    problemReducer = True
    edgecase = False
    y = [int(n) for n in x.split()]
    if y[0] < y[1]:
        y.reverse()
    if(evaluateReport(y)):
        safe += 1
    else:
        oldY = y.copy()
        for x in range(len(oldY)):
            y = oldY.copy()
            y.pop(x)
            if(evaluateReport(y)):
                safe += 1
                break
            y.reverse()
            if(evaluateReport(y)):
                safe += 1
                break

print(safe)
