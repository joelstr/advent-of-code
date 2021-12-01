f = open("Day9/input.txt", "r")
# f = open("Day9/test.txt", "r")
inputData = f.read().splitlines()
inputData = list(map(int,inputData))

preamble = 25

# validNumbers = []

# for i in range(0,preamble):
#     for j in range(0,preamble):
#         if i != j:
#             validNumbers.append(inputData[i]+inputData[j])

# for i in range(preamble,len(inputData)):
#     if inputData[i] in validNumbers:
#         validNumbers = validNumbers[preamble-1:]
#         for j in range(i,preamble+i-1):
#             validNumbers.append(inputData[i]+inputData[j])
#     else:
#         print(inputData[i])
#         break

for i in range(preamble,len(inputData)):
    sumExist = False
    for j in range(i-preamble,i):
        for k in range(i-preamble,i):
            if j != k:
                if inputData[i] == inputData[j]+inputData[k]:
                    sumExist = True
                    break
    if not sumExist:
        print(inputData[i])
        invalidNumber = inputData[i]
        break

minIdx = 0
maxIdx = 1
numSum = inputData[minIdx]+inputData[maxIdx]

while True:
    if numSum < invalidNumber:
        maxIdx += 1
        numSum += inputData[maxIdx]
    elif numSum > invalidNumber:
        numSum -= inputData[minIdx]
        minIdx += 1
    elif numSum == invalidNumber:
        print(min(inputData[minIdx:maxIdx+1])+max(inputData[minIdx:maxIdx+1]))
        break
