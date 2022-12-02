# Part 1

f = open("input.txt", "r")
inputData = f.readlines()
points = 0

for x in inputData:
    result = [y.strip() for y in x.split(" ")]
    enemy = ord(result[0])-64
    player = ord( result[1])- ord('W')
    points += player
    if player ==  enemy:
        points += 3
    elif player == 1 and enemy == 3:
        points += 6
    elif player == 3 and enemy == 1:
        points += 0
    elif player > enemy:
        points += 6
print(points)


# Part 2
points = 0

for x in inputData:
    result = [y.strip() for y in x.split(" ")]
    enemy = ord(result[0])-64
    player = result[1]
    if player == 'Z': # Win
        points += 6
        if enemy == 3:
            points += 1
        else:
            points += enemy + 1
    elif player == 'Y': # Draw
        points += 3+enemy

    else:
        if enemy == 1:
            points += 3
        else:
            points += enemy - 1

print(points)