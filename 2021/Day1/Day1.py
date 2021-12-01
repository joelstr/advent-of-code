f = open("input.txt", "r")
inputData = f.readlines()
depth = 0
lastvalue = 1000000

for x in range(len(inputData)-3):
    window1 = int(inputData[x])+int(inputData[x+1])+int(inputData[x+2])
    window2 = int(inputData[x+3])+int(inputData[x+1])+int(inputData[x+2])
    if window2 > window1:
        depth += 1
print(depth)
#     for y in inputData:
#         # print(x+y)
#         # print(y)
#         for z in inputData:
#             if int(x)+int(y)+int(z) == 2020:
#                 print(int(x)*int(y)*int(z))
# # print(inputData)