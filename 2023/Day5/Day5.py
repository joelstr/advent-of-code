import re

# Part 1

f = open("input.txt", "r")
# f = open("testdata.txt", "r")
inputData = f.read()
inputData = inputData.split('\n\n')

seeds = list(map(int,inputData[0].split(':')[1].split()))
seedToSoil = [list(map(int,x.split())) for x in inputData[1].split('\n')[1:]]
soilToFertilizer = [list(map(int,x.split())) for x in inputData[2].split('\n')[1:]]
fertilizerToWater = [list(map(int,x.split())) for x in inputData[3].split('\n')[1:]]
waterToLight = [list(map(int,x.split())) for x in inputData[4].split('\n')[1:]]
lightToTemp = [list(map(int,x.split())) for x in inputData[5].split('\n')[1:]]
tempToHumid = [list(map(int,x.split())) for x in inputData[6].split('\n')[1:]]
humidToLoc = [list(map(int,x.split())) for x in inputData[7].split('\n')[1:]]

def findNextId(id, currentMap):
    for x in currentMap:
        if id >= x[1] and id < x[1]+x[2]:
            return x[0]-x[1]+id
    return id

allLocations = list()

# Part 1

minLocation = 0
for seed in seeds:
    soil = findNextId(seed, seedToSoil)
    fert = findNextId(soil, soilToFertilizer)
    water = findNextId(fert, fertilizerToWater)
    light = findNextId(water, waterToLight)
    temp = findNextId(light, lightToTemp)
    humid = findNextId(temp, tempToHumid)
    loc = findNextId(humid, humidToLoc)
    if minLocation == 0 or loc < minLocation:
        minLocation = loc
print(minLocation)


# Part 2
# This takes like 8 hours to run, should have been solved using intervals instead.

minLocation = 0
for i in range(0,len(seeds),2):
    for seed in range(seeds[i],seeds[i]+seeds[i+1]):
        soil = findNextId(seed, seedToSoil)
        fert = findNextId(soil, soilToFertilizer)
        water = findNextId(fert, fertilizerToWater)
        light = findNextId(water, waterToLight)
        temp = findNextId(light, lightToTemp)
        humid = findNextId(temp, tempToHumid)
        loc = findNextId(humid, humidToLoc)
        if minLocation == 0 or loc < minLocation:
            minLocation = loc
print(minLocation)