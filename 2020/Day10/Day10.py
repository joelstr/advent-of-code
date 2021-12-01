f = open("Day10/input.txt", "r")
# f = open("Day10/test.txt", "r")
# f = open("Day10/smalltest.txt", "r")
inputData = f.read().splitlines()
inputData = list(map(int,inputData))

inputData.sort()

jolt1 = 0
jolt3 = 0
if inputData[0] == 1:
    jolt1 += 1
elif inputData[0] == 3:
    jolt3 += 1
for i in range(1,len(inputData)):
    if inputData[i]-inputData[i-1] == 1:
        jolt1 += 1
    elif inputData[i]-inputData[i-1] == 3:
        jolt3 += 1
    elif inputData[i]-inputData[i-1] > 3:
        print("Error in data")

print(jolt1*(jolt3+1))

# combinations = 1

# for i in range(0,len(inputData)):
#     try:
#         if inputData[i+3]-inputData[i] < 4:
#             combinations += 2
#         elif inputData[i+2]-inputData[i] < 4:
#             combinations += 1
#     except:
#         print("End of array")
#     # combinations *= factor

combinations = 0
nodes = []
nodes.append(0)
while nodes:
    if nodes[0] == len(inputData)-1:
        combinations += 1
    else:
        nodes.append(nodes[0]+1)
        if nodes[0]+2 < len(inputData):
            if inputData[nodes[0]+2]-inputData[nodes[0]] < 4:
                nodes.append(nodes[0]+2)
            if nodes[0]+3 < len(inputData):
                if inputData[nodes[0]+3]-inputData[nodes[0]] < 4:
                    nodes.append(nodes[0]+3)
    nodes.pop(0)


print(combinations)