# Part 1

f = open("input.txt", "r")
inputData = f.readlines()
calories = 0
maxCalories = -1

for x in inputData:
    if x == '\n':
        if calories > maxCalories:
            maxCalories = calories
        calories = 0
    else:
        calories += int(x)


print(maxCalories)

#Part 2

calories = 0
top1Calories = -1
top2Calories = -1
top3Calories = -1

for x in inputData:
    if x == '\n':
        if calories > top1Calories:
            top3Calories = top2Calories
            top2Calories = top1Calories
            top1Calories = calories
        elif calories > top2Calories:
            top3Calories = top2Calories
            top2Calories = calories
        elif calories > top3Calories:
            top3Calories = calories

        calories = 0
    else:
        calories += int(x)


print(top1Calories + top2Calories + top3Calories)