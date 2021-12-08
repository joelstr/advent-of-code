import os

print(os.path.dirname(__file__))
filename = os.path.dirname(__file__) + "\\input.txt"
print(filename)
f = open(filename, "r")
inputData = f.readlines()

def findwinner(boards, draws):
    for d in draws:
        for index, board in enumerate(boards):
            for i in range(5):
                for j in range(5):
                    # print(board)
                    if board[i][j] == d:
                        board[i][j] = 'X'
                        # if all(flag == 'X' for flag in board[:][j]) or all(flag[j] == 'X' for flag in board[:][:]):
                        if all(flag == 'X' for flag in board[i][:]) or all(flag[j] == 'X' for flag in board[:][:]):
                            # print("We found a winner")
                            return board, d, index




draws = inputData[0].strip()
draws = draws.split(',')
# print(len(inputData))
boards = list()
for i in range(0,round((len(inputData)-1)/6)):
    board = list()
    x = list()
    for j in range(6*i+2,6*i+7):
        x.append(inputData[j].strip().split())
        # if i == 2:
            # for n in inputData[]

            # print(inputData[j].strip().split())
    board.append(x)
    boards.append(x)

winner, draw, index = findwinner(boards, draws)
print("Winner: " + str(winner))
print(draw)
sum = 0
for i in range(5):
    for j in range(5):
        if winner[i][j] != 'X':
            sum += int(winner[i][j])
print(sum)
print(sum*int(draw))

# Part 2
boards.pop(index)
while len(boards) > 0:
    winner, draw, index = findwinner(boards, draws)
    boards.pop(index)
sum = 0
for i in range(5):
    for j in range(5):
        if winner[i][j] != 'X':
            sum += int(winner[i][j])
print("Loser: " + str(winner))
print(draw)
print(sum)
print(sum*int(draw))