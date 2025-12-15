import numpy as np
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Part 1

# f = open("2025/Day2/input.txt", "r")
# f = open("2025/Day2/testdata.txt", "r")
f = open(os.path.join(__location__, 'input.txt'))
# f = open(os.path.join(__location__, 'testdata.txt'))
inputData = f.readlines()

def isInvalid(number):
    for i in range(len(str(x))):
            # print(number)
            number = str(x)
            # number = number.replace(str(str(x)[0:i]),"")

            # if (number == ""):
            if (number[0:int(len(number)/2)] == number[int(len(number)/2):]):
                # print(f"Number {x} is invalid due to " + str(x)[0:i] + " repeating")
                return True
    return False

ranges = inputData[0].strip().split(',')


invalidData = 0

# testvariable = "101"
# print(testvariable)
# print(testvariable[0:int(len(testvariable)/2)])
# print(testvariable[int(len(testvariable)/2):])

# if (testvariable[0:int(len(testvariable)/2)] == testvariable[int(len(testvariable)/2+1):]):
#     print(f"Number {x} is invalid due to " + str(x)[0:i] + " repeating")

for currentRange in ranges:
    bounds = currentRange.split('-')
    start = int(bounds[0])
    end = int(bounds[1])
    for x in range(start, end + 1):
        if isInvalid(x):
            # print(f"Invalid number found: {x}")
            invalidData += x

print(invalidData)


# Part 2

