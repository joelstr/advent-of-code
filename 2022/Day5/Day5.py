# Part 1

f = open("input.txt", "r")
inputData = f.readlines()
crates = ["","","","","","","","",""]

cratedata = [x for x in inputData[0:8]]

for x in reversed(cratedata):
    for i in range(0,9):
        crateindex = 1 + i*4
        if x[crateindex] != " ":
            crates[i]= crates[i] + x[crateindex]

crates2 = crates.copy()

def move1(fr, to):
    crates[to] += crates[fr][-1]
    crates[fr]=crates[fr][:-1]

def move(n,fr,to):
    for i in range(n):
        move1(fr,to)

def movestack(n,fr,to):
    crates2[to] += crates2[fr][-n:]
    crates2[fr] = crates2[fr][:-n]

# Part 1

for x in crates:
    print(x)

for x in inputData[10:]:
    moves = [int(s) for s in x.split() if s.isdigit()]
    move(moves[0],moves[1]-1,moves[2]-1)
    print()

for x in crates:
    print(x)

print()
# Part 2
for x in crates2:
        print(x)

for x in inputData[10:]:
    moves = [int(s) for s in x.split() if s.isdigit()]
    movestack(moves[0],moves[1]-1,moves[2]-1)

print()
for x in crates2:
        print(x)