f = open("Day6/input.txt", "r")
# f = open("Day6/test.txt", "r")
inputData = f.readlines()

answers = 0
answerlist = []
for l in inputData:
    if l == '\n':
        answers += len(answerlist)
        answerlist.clear()
    else:
        l = l.replace('\n','')
        for c in l:
            if c not in answerlist:
                answerlist.append(c)
if len(answerlist) != 0:
    answers += len(answerlist)
    answerlist.clear()
print(answers)

answers = 0
groupsize = 0
for l in inputData:
    if l == '\n':
        for c in range(ord('a'),ord('z')+1):
            if answerlist.count(chr(c)) == groupsize:
                answers += 1
        answerlist.clear()
        groupsize = 0
    else:
        groupsize += 1
        l = l.replace('\n','')
        for c in l:
            answerlist.append(c)
if len(answerlist) != 0:
    for c in range(ord('a'),ord('z')):
            if answerlist.count(chr(c)) == groupsize:
                answers += 1
print(answers)