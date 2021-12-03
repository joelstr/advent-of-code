f = open("input.txt", "r")
inputData = f.readlines()
data = [0]*(len(inputData[0])-1)
oxygen = inputData.copy()
# print(data)
for x in inputData:
    for i, s in enumerate(x):
        if s == "1":
            data[i] += 1

result = list()
for n in data:
    if n > len(inputData)/2:
        result.append('1')
    else:
        result.append('0')
result = ''.join(result)
# print(int(result,2) * (~int(result,2) & 0xfff))

# Part 2
oxygen = inputData.copy()
co2 = inputData.copy()
while len(oxygen) > 1:
    for i in range(len(inputData[0])):
        total = 0
        for x in oxygen:
            try:
                if x[i] == '1':
                    total += 1
            except:
                print(" AJAJAJAJA " +x)
                print(i)
        print("Totalt: " + str(total))
        print("Oxygen: " + str(len(oxygen)))
        if total >= len(oxygen)/2:
            print("Removing 0")
            debug = 0
            for j, x in reversed(list(enumerate(oxygen))):
                if x[i] == '0':
                    # print(j)
                    debug += 1
                    oxygen.pop(j)
            print("Removed " + str(debug) + " zeros")
        else:
            print("Removing 1")
            debug = 0
            # print(len(oxygen))
            for j, x in reversed(list(enumerate(oxygen))):
                # print(j)
                if x[i] == '1':

                    debug += 1
                    oxygen.pop(j)
            print("Removed " + str(debug) + " ones")
print(oxygen)
print(int("".join(oxygen),2))
oxygenresult = int("".join(oxygen),2)
print("\n")
print("Switching to co2")
print("Starting with " + str(len(co2)))
co2 = inputData.copy()
while len(co2) > 1:
    for i in range(len(inputData[0])):
        print("Iteration " + str(i))
        total = 0
        for x in co2:
            try:
                if x[i] == '1':
                    total += 1
            except:
                print(" AJAJAJA" + x)
                print(i)

        print("Totalt: " + str(total))
        print("Co2: " + str(len(co2)))
        if total <= len(co2)/2:
            print("Removing 1")
            debug = 0
            for j, x in reversed(list(enumerate(co2))):
                if x[i] == '1':
                    debug += 1
                    co2.pop(j)


            print("Removed " + str(debug) + " ones")
        else:
            debug = 0
            print("Removing 0")
            for j, x in reversed(list(enumerate(co2))):
                if x[i] == '0':
                    debug += 1
                    co2.pop(j)

            print("Removed " + str(debug) + " zeros")

print(co2)
print(int("".join(co2),2))
co2result = int("".join(co2),2)

print(co2result*oxygenresult)