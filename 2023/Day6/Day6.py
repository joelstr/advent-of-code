import math

# Part 1

f = open("input.txt", "r")
# f = open("testdata.txt", "r")
inputData = f.readlines()

time = list(map(int,inputData[0].split(':')[1].split()))
distance = list(map(int,inputData[1].split(':')[1].split()))

# x*(time-x) > distance => x^2-time*x+distance = 0
# x = time/2 +- sqrt((time/2)^2-distance)

total = 1

for i in range(len(time)):
    min = math.floor(time[i]/2-math.sqrt((time[i]/2)**2 - distance[i])+1)
    max = math.ceil(time[i]/2+math.sqrt((time[i]/2)**2 - distance[i])-1)
    total *= (max-min+1)
    
print(total)

# Part 2

time2 = int(inputData[0].replace(" ", "").split(':')[1])
distance2 =int(inputData[1].replace(" ", "").split(':')[1])

min = math.floor(time2/2-math.sqrt((time2/2)**2 - distance2)+1)
max = math.ceil(time2/2+math.sqrt((time2/2)**2 - distance2)-1)
print(max-min+1)