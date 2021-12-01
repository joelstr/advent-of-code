from itertools import permutations 

inputdata = []
with open("input.txt", "r") as filestream:
    for line in filestream:
        for num in line.split(","):
            inputdata.append(num)
size = len(inputdata)
for i in range(size,size+1000):
    inputdata.append(0)
inputdata2 = inputdata.copy()
i = 0
basevalue = 0

def getparams(opcode,i):
    if opcode == "1":
        return int(inputdata[i])
    elif opcode == "2": 
        return int(inputdata[basevalue+int(inputdata[i])])
    elif opcode == "0":
        return int(inputdata[int(inputdata[i])])
    else:
        print("This is very bad")

def runcode(inputvalue):
    global i 
    global k
    global inputdata
    global basevalue
    while inputdata[i] != "99":
        # print ("Executing code " + str(i) + " which is " + str(inputdata[i]))
        tmp = "0000" + inputdata[i]
        if tmp[-1] == "1":
            param1 = getparams(tmp[-3],i+1)
            param2 = getparams(tmp[-4],i+2)
            inputdata[int(inputdata[i+3])] = str(param1 + param2)
            i += 4
        elif tmp[-1] == "2":
            param1 = getparams(tmp[-3],i+1)
            param2 = getparams(tmp[-4],i+2)
            inputdata[int(inputdata[i+3])] = str(param1 * param2)
            i += 4
        elif tmp[-1] == "3":
            inputdata[int(inputdata[i+1])] = str(inputvalue)
            i += 2
        elif tmp[-1] == "4":
            param = getparams(tmp[-3],i+1)
            i += 2
            print(str(i) + " " + str(param))
        elif tmp[-1] == "5":
            param1 = getparams(tmp[-3],i+1)
            param2 = getparams(tmp[-4],i+2)
            if param1:
                i = param2
            else:
                i += 3
        elif tmp[-1] == "6":
            param1 = getparams(tmp[-3],i+1)
            param2 = getparams(tmp[-4],i+2)
            if param1:
                i += 3
            else:
                i = param2
        elif tmp[-1] == "7":
            param1 = getparams(tmp[-3],i+1)
            param2 = getparams(tmp[-4],i+2)
            if param1 < param2:
                inputdata[int(inputdata[i+3])] = str(1)
            else:
                inputdata[int(inputdata[i+3])] = str(0)
            i += 4
        elif tmp[-1] == "8": 
            param1 = getparams(tmp[-3],i+1)
            param2 = getparams(tmp[-4],i+2)
            if param1 == param2:
                inputdata[int(inputdata[i+3])] = str(1)
            else:
                inputdata[int(inputdata[i+3])] = str(0)
            i += 4
        elif tmp[-1] == "9":
            param = getparams(tmp[-3],i+1)
            basevalue += param
            # print(str(i) + " " + str(basevalue))
            i += 2
        else:
            print("Oops!")
            break
    print("Done")

inputvalue = 1
i = 0
k = 0
runcode(inputvalue)