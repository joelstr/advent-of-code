import math

# Part 1

f = open("2023/Day8/input.txt", "r")
# f = open("2023/Day8/testdata.txt", "r")
inputData = f.readlines()

instructions = inputData[0]

nodes = list()

for x in inputData[2:]:
    loc = x.split('=')[0].strip()
    left = x.split('=')[1].split(',')[0][2:]
    right = x.split('=')[1].split(',')[1][1:4]
    nodes.append([loc, left, right])


instructions = instructions.strip()

# Part 1
 
node = 'AAA'
steps = 0
while node != 'ZZZ':
    step = instructions[0]
    instructions = instructions[1:] + instructions[0]
    steps += 1
    for x in nodes:
        if x[0] == node:
            if step == 'R':
                node = x[2]
            else:
                node = x[1]
            break

print(steps)

# Part 2

searching = True

currentNodes = list()
allNodes = list()

for x in nodes:
    if x[0][2] == 'A':
        currentNodes.append(x[0])
allNodes.append(currentNodes)
locations = [x[0] for x in nodes]

steps = 0
while searching:
    nodeList = list()
    searching = False
    step = instructions[0]
    instructions = instructions[1:] + instructions[0]
    steps += 1
    for x in currentNodes:
        if step == 'R':
            nodeList.append(nodes[locations.index(x)][2])
            if nodeList[-1][2] != 'Z':
                searching = True
        else:
            nodeList.append(nodes[locations.index(x)][1])
            if nodeList[-1][2] != 'Z':
                searching = True
    currentNodes = nodeList

    # Debug testing
    # if currentNodes in allNodes or len(currentNodes) > 600:
    #     print("We're walking in a circle")
    #     break
    # else:
    #     allNodes.append(currentNodes)

print(steps)

