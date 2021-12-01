f = open("input.txt", "r")
inputData = f.readlines()
for x in inputData:
    # inputData.append(x)
    # print(x)
    for y in inputData:
        # print(x+y)
        # print(y)
        for z in inputData:
            if int(x)+int(y)+int(z) == 2020:
                print(int(x)*int(y)*int(z))
# print(inputData)