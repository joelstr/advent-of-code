# Part 1

f = open("input.txt", "r")
inputData = f.readlines()
inputData = inputData[0]
number = 0

# Part 1

for i in range(3,len(inputData)):
    # print(inputData[i])
    # print(inputData[i-3:i+1])
    tmplist = list(dict.fromkeys(list(inputData[i-3:i+1])))
    if len(tmplist)==4:
        number = i+1
        break

print(number)

# Part 2
number = 0
for i in range(13,len(inputData)):
    # print(inputData[i])
    # print(inputData[i-3:i+1])
    tmplist = list(dict.fromkeys(list(inputData[i-13:i+1])))
    if len(tmplist)==14:
        number = i+1
        break

print(number)