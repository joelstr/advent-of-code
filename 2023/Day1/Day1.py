# Part 1

f = open("input.txt", "r")
# f = open("testdata.txt", "r")
inputData = f.readlines()
value = list()

tmp = 0

for x in inputData:
    for y in x:
        if y.isdigit():
            tmp = 10*int(y)
            break
    for y in reversed(x):
        if y.isdigit():
            tmp = tmp+int(y)
            break
    value.append(tmp)
print(sum(value))

#Part 2

value2 = list()
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4','5','6','7','8','9']
lowtmp = 0
hightmp = 0

for x in inputData:
    lowindex = 1000
    highindex = -1
    for num in numbers:
        try:
            if x.index(num) < lowindex:
                lowindex = x.index(num)
                if num.isdigit():
                    lowtmp = int(num)*10
                else:
                    lowtmp = (numbers.index(num)+1)*10
            if x.rfind(num) > highindex:
                highindex = x.rfind(num)
                if num.isdigit():
                    hightmp = int(num)
                else:
                    hightmp = (numbers.index(num)+1)
        except:
            1+1
    value2.append(lowtmp+hightmp)


print(sum(value2))
