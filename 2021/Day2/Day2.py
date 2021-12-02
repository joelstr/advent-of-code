f = open("input.txt", "r")
inputData = f.readlines()
depth = 0
horizontal = 0
aim = 0

for x in inputData:
    x = x.split()
    if x[0] == "forward":
        horizontal += int(x[1])
        depth += aim*int(x[1])
    if x[0] == "down":
        aim += int(x[1])
    if x[0] == "up":
        aim -= int(x[1])
print(depth*horizontal)