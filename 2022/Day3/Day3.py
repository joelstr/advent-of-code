# Part 1

from curses.ascii import isupper
from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    # print each string in args
    #c = copy.deepcopy(args)
    #for a in c:
    #    print(list(a))
    return zip_longest(*args, fillvalue=fillvalue)

f = open("input.txt", "r")
inputData = f.readlines()
prio = 0

for x in inputData:
    size = int((len(x)+1)/2)-1
    comp1 = x[0:size]
    comp2 = x[size:]
    for c in comp1:
        if c in comp2:
            if c.isupper():
                prio += 26
                c=c.lower()
            prio += ord(c)-ord('a')+1
            break
print(prio)

# Part 2

prio = 0
for x, y, z in grouper(inputData,3):
    for c in x:
        if c in y and c in z:
            if c.isupper():
                prio += 26
                c=c.lower()
            prio += ord(c)-ord('a')+1
            break

print(prio)