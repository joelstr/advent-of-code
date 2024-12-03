import re

# Part 1

f = open("2024/Day3/input.txt", "r")
# f = open("2024/Day3/testdata.txt", "r")
inputData = f.read()

def parseMul(x):
    x = x[4:-1]
    x = x.split(",")
    return int(x[0]) * int(x[1])

def remove_str_start_end(s, start, end):
    return s[:start] + s[end + 1:]

x = re.findall(r"mul\(\d+,\d+\)", inputData)

uncorrupted = 0
for y in x:
    uncorrupted += parseMul(y)

print(uncorrupted)

#Part 2

x = re.finditer(r"do[n't]*\(\)", inputData)
dontFound = False
dontstart = []
doend = []
for r in x:
    if not dontFound:
        if r.group() == "don't()":
            dontFound = True
            dontstart.append(r.end())
    if dontFound:
        if r.group() == "do()":
            dontFound = False
            doend.append(r.start())

if len(dontstart) > len(doend):
    inputData = inputData[:dontstart[-1]]
    dontstart.pop(-1)

dontstart.reverse()
doend.reverse()

for x in range(len(doend)):
    inputData = remove_str_start_end(inputData, dontstart[x], doend[x])



x = re.findall(r"mul\(\d+,\d+\)", inputData)
uncorrupted = 0
for y in x:
    uncorrupted += parseMul(y)

print(uncorrupted)