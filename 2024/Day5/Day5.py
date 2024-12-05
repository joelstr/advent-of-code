import numpy as np
import re

# Part 1

f = open("2024/Day5/input.txt", "r")
# f = open("2024/Day5/testdata.txt", "r")
inputData = f.read()

[rules, prints] = inputData.split("\n\n")

it = iter(re.split(r'[|\n]', rules))
rules = list(zip(it, it))
# first = []
# second = []
# for x in rules.split("\n"):
#     first.append(x.split("|")[0])
#     second.append(x.split("|")[1])

actualPrints = prints.split("\n")
wrongPrints = []
for x in prints.split("\n"):
    printed = []
    notOk = False
    for page in x.split(","):
        values = [item for item in rules if item[1] == page]
        for y in values:
            if y[0] not in printed and y[0] in x.split(','):
                actualPrints.remove(x)
                wrongPrints.append(x)
                notOk = True
                break
        if notOk:
            break
#         if page in second:
#             if first[second.index(page)] not in printed and first[second.index(page)] in x.split(','):
#                 actualPrints.remove(x)
#                 break
        printed.append(page)

totalValue = 0
for x in actualPrints:
    totalValue += int(x.split(",")[int((len(x.split(","))-1)/2)])

print(totalValue)

#Part 2
correctedPrints = []
for x in wrongPrints:
    pageList = x.split(",")
    printed = []

    for i in range(len(pageList)):
        pageNotOk = True
        while pageNotOk:
            Ok = True
            values = [item for item in rules if item[1] == pageList[i]]
            for y in values:
                if y[0] not in printed and y[0] in pageList:
                    pageList.append(pageList.pop(i))
                    Ok = False
                    break
            if Ok:
                pageNotOk = False
        printed.append(pageList[i])
    correctedPrints.append(pageList)

totalValue = 0
for x in correctedPrints:
    totalValue += int(x[int((len(x)-1)/2)])

print(totalValue)