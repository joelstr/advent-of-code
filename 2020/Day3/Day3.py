from operator import xor
f = open("input.txt", "r")
# f = open("test.txt", "r")
inputData = f.readlines()
product = 1

# print(inputData[1])
def RideHill(right, down):
    column = 0
    row = down
    tree = 0
    hole = 0
    dumt = 0
    # print(len(inputData))
    # print(len(inputData[1]))
    while row < len(inputData):
        line = inputData[row]
        row += down
        # print("New Iteration:")
        column += right
        # print(line)
        # print(column)
        # print(len(line))
        # print("Column: " + str(column % (len(line)-1)))
        if line[column % (len(line)-1)] == '#':
            tree += 1
        elif line[column % (len(line)-1)] == '.':
            hole += 1
        else:
            dumt += 1
        # print("Trees: " + str(tree))
        # print()

    print(tree)
    # print(hole)
    # print(dumt)
    return tree

product *= RideHill(1,1)
product *= RideHill(3,1)
product *= RideHill(5,1)
product *= RideHill(7,1)
product *= RideHill(1,2)
print(product)