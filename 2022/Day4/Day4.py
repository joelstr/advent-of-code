# Part 1

f = open("input.txt", "r")
inputData = f.readlines()
overlaps = 0

for x in inputData:
    pairs = [y.strip() for y in x.split(",")]
    range1 = pairs[0].split('-')
    range1 = range(int(range1[0]),int(range1[1])+1)
    range2 = pairs[1].split('-')
    range2 = range(int(range2[0]),int(range2[1])+1)
    if set(range1).issubset(range2) or set(range2).issubset(range1):
        overlaps += 1
print(overlaps)

# Part 2

overlaps = 0
for x in inputData:
    pairs = [y.strip() for y in x.split(",")]
    range1 = pairs[0].split('-')
    range1 = range(int(range1[0]),int(range1[1])+1)
    range2 = pairs[1].split('-')
    range2 = range(int(range2[0]),int(range2[1])+1)
    if set(range1).intersection(range2) or set(range2).intersection(range1):
        overlaps += 1
print(overlaps)