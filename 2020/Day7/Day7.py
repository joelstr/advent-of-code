f = open("Day7/input.txt", "r")
# f = open("Day6/test.txt", "r")
inputData = f.readlines()
outerbags = []
startbag = "shiny gold"

def FindOuterBags(bag):
    global outerbags
    for l in inputData:
        bagtype = l.split(' contain ')
        if bag in bagtype[1]:
            if bagtype[0].replace(' bags','') not in outerbags:
                outerbags.append(bagtype[0].replace(' bags',''))
            FindOuterBags(bagtype[0].replace(' bags',''))
        
FindOuterBags(startbag)
print(len(outerbags))