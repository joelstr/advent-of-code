from operator import xor
f = open("input.txt", "r")
inputData = f.readlines()
correctPasswords = 0
correctNewPasswords = 0
for x in inputData:
    lettercount = 0
    rule = x.split(':')
    letter = rule[0].split(' ')
    for i in rule[1]:
        if i == letter[1]:
            lettercount += 1
    limits = letter[0].split('-')
    if lettercount >= int(limits[0]) and lettercount <= int(limits[1]):
        correctPasswords += 1
print(correctPasswords)

for x in inputData:
    lettercount = 0
    rule = x.split(':')
    letter = rule[0].split(' ')
    limits = letter[0].split('-')
    if xor(bool(letter[1] == rule[1][int(limits[0])]), bool(letter[1] == rule[1][int(limits[1])])):
        correctNewPasswords += 1
print(correctNewPasswords)