# Part 1

f = open("input.txt", "r")
# f = open("testdata.txt", "r")
inputData = f.readlines()
totalId = 0
totalPower = 0

def getData(x):
    gameId = int(x.split(':')[0].split()[1])
    red = list()
    green = list()
    blue = list()
    for y in x.split(':')[1].split(';'):
        for color in y.split(','):
            if color.split()[1] == 'red':
                red.append(int(color.split()[0]))
            if color.split()[1] == 'green':
                green.append(int(color.split()[0]))
            if color.split()[1] == 'blue':
                blue.append(int(color.split()[0]))
    return gameId, red, green, blue

for x in inputData:
    gameId, red, green, blue = getData(x)
    if max(red) <=12 and max(green) <= 13 and max(blue) <= 14:
        print(gameId)
        totalId += gameId
    power = max(red)*max(blue)*max(green)
    totalPower += power

print(totalId)
print(totalPower)