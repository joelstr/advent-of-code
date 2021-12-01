f = open("input.txt","r")
inputdata = f.readlines()
inputdata2 = inputdata.copy()
orbits = []

def FindOrbit(name):
    orbitting=[]
    global inputdata
    inputdatatmp = inputdata.copy()
    for p in inputdata:
        if p[0:3] == name:
            orbitting.append(p[4:-1])
            inputdatatmp.remove(p)
    inputdata = inputdatatmp.copy()
    return orbitting

def FindOrbitting(name):
    orbits=[]
    global inputdata
    inputdatatmp = inputdata.copy()
    for p in inputdata:
        if p[4:-1] == name:
            orbits.append(p[0:3])
            inputdatatmp.remove(p)
    inputdata = inputdatatmp.copy()
    return orbits

orbits = FindOrbit("COM")
crc = 1
i = 2
while inputdata:
    orbittmp = []
    orbittmp.clear()
    for p in orbits:
        orbittmp+= FindOrbit(p)
    orbits = orbittmp.copy()
    crc += len(orbits)*i
    orbittmp.clear()
    i += 1
    if not orbits:
        print(inputdata)
        break
print(crc)


# -------- Part 2 ---------
inputdata = inputdata2.copy()
orbits = FindOrbitting("YOU")
print(orbits)
crc = 1
i = 0
while inputdata:
    orbittmp = []
    orbittmp.clear()
    for p in orbits:
        orbittmp+= FindOrbit(p)
        orbittmp+= FindOrbitting(p)
    orbits = orbittmp.copy()
    crc += len(orbits)*i
    orbittmp.clear()
    if "SAN" in orbits:
        print(i)
    i += 1
    if not orbits:
        print(inputdata)
        break
print(crc)