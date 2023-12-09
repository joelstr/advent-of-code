import time
import math


start_time = time.time()

# Part 1

f = open("2023/Day8/input.txt", "r")
# f = open("2023/Day8/testdata.txt", "r")
inputData = f.readlines()

instructions = inputData[0]

nodes = {}
currentNodes = list()
endNodes = list()

for x in inputData[2:]:
    loc = x.split('=')[0].strip()
    left = x.split('=')[1].split(',')[0][2:]
    right = x.split('=')[1].split(',')[1][1:4]
    nodes[loc] = (left, right)
    if loc[2] == 'A':
        currentNodes.append(loc)    
    if loc[2] == 'Z':
        endNodes.append(loc)

instructions = instructions.strip()

# Part 1

def Part1(): 
    global instructions
    node = 'AAA'
    steps = 0
    while node != 'ZZZ':
        step = instructions[0]
        instructions = instructions[1:] + instructions[0]
        steps += 1
        if step == 'R':
            node = nodes[node][1]
        else:
            node = nodes[node][0]

    print(steps)

# Part 2

# This only works because input data is very nice

steps = 0
def Part2():
    global instructions, currentNodes, steps

    steplist = list()

    for x in currentNodes:
        visitedNodes = {}
        node = x
        found = 0
        steps = 0
        nodesteps = list()
        while found < 5:
            step = instructions[steps%len(instructions)]
            steps += 1
            visitedNodes[node] = steps%len(instructions)
            if step == 'R':
                node = nodes[node][1]
            else:
                node = nodes[node][0]
            if node in endNodes:
                nodesteps.append(steps)
                found += 1
        steplist.append(nodesteps[0])
        # This is just to confirm that input data is nice
        print("Done with %s. First end after %s steps. Next differences are %s %s %s and %s" % (x, nodesteps[0], nodesteps[1]-nodesteps[0], nodesteps[2]-nodesteps[1], nodesteps[3]-nodesteps[2], nodesteps[4]-nodesteps[3]))

    print(math.lcm(*steplist))

if __name__ == '__main__':
    try:
        Part1()
        pass
    except KeyboardInterrupt:
       print("Run interrupted during part 1 after %s seconds" % (time.time() - start_time))

    try:
        Part2()
    except KeyboardInterrupt:
       print("Run interrupted during part 2 after %s seconds" % (time.time() - start_time))
       print("Then we had moved %s steps" % steps)


    print("Runtime %s seconds" % (time.time() - start_time))