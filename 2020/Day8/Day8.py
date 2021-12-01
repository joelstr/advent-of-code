f = open("Day8/input.txt", "r")
# f = open("Day8/test.txt", "r")
inputData = f.readlines()

index = 0
accumulator = 0
oldindex = []

while True:
    if index in oldindex:
        break
    else:
        oldindex.append(index)
    data = inputData[index].split(' ')
    if data[0] == 'acc':
        accumulator += int(data[1])
        index += 1
    elif data[0] == 'jmp':
        index += int(data[1])
    elif data[0] == 'nop':
        index += 1
    else:
        print("Not good")

print(accumulator)


index = 0
accumulator = 0
oldindex.clear()
# tmpboot = inputData.copy()
print(len(inputData))

for i in range(0,len(inputData)):
    while True:
        if index in oldindex or index >= len(inputData):
            break
        else:
            oldindex.append(index)
        data = inputData[index].split(' ')
        if data[0] == 'acc':
            accumulator += int(data[1])
            index += 1
        elif data[0] == 'jmp':
            if index == i:
                index += 1
            else:
                index += int(data[1])
        elif data[0] == 'nop':
            if index == i:
                index += int(data[1])
            else:
                index += 1
        else:
            print("Not good")
    if index >= len(inputData):
        break
    else:
        index = 0
        accumulator = 0
        oldindex.clear()

print(accumulator)