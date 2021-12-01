f = open("Day5/input.txt", "r")
# f = open("test.txt", "r")
inputData = f.readlines()

seats = []
for l in inputData:
    l = l.replace('\n','')
    i = 64
    j = 4
    rowmin = 0
    rowmax = 127
    seatmin = 0
    seatmax = 7
    # print(l)
    for c in l:
        if c == 'F':
            rowmax -= i
            i /= 2
        elif c == 'B':
            rowmin += i
            i /= 2
        elif c == 'L':
            seatmax -= j
            j /= 2
        elif c == 'R':
            seatmin += j
            j /= 2
        else:
            print('Something went wrong')
    if (rowmax == rowmin) and (seatmin == seatmax):
        seats.append(rowmax * 8 + seatmax)
        # print("It worked")
    else:
        print("You messed up")

max(seats)
print(max(seats))

seats.sort()
# print(seats)
for i in range(85,891):
    if i not in seats:
        print(i)