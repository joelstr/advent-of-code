import string
f = open("input.txt", "r")
# f = open("test.txt", "r")
inputData = {}
inputData = f.read().split('\n\n')
# print(inputData)
correct = 0
approvedPassports = 0
for line in inputData:
    if 'byr' in line and 'iyr' in line and 'eyr' in line and 'hgt' in line and 'hcl' in line and 'ecl' in line and 'pid' in line:
        correct += 1
        # line = line.replace('\n',' ')
        parts = line.replace('\n',' ').split(' ')
        approved = True
        for part in parts:
            if 'byr' in part:
                data = part.split(':')
                if int(data[1])<1920 or int(data[1])>2020:
                    approved = False
                    break
            elif 'iyr' in parts:
                data = part.split(':')
                if int(data[1])<2010 or int(data[1])>2020:
                    approved = False
                    break
            elif 'eyr' in parts:
                data = part.split(':')
                if int(data[1])<2020 or int(data[1])>2030:
                    approved = False
                    break
            elif 'hgt' in parts:
                data = part.split(':')
                if data[1].endswith('cm'):
                    if int(data[1].replace('cm',''))<150 or int(data[1].replace('cm',''))>193:
                        approved = False
                        break
                elif data[1].endswith('in'):
                    if int(data[1].replace('in',''))<59 or int(data[1].replace('in',''))>76:
                        approved = False
                        break
                else:
                    approved = False
                    break
            elif 'hcl' in parts:
                data = part.split(':')
                if data[1].startswith('#'):
                    if len(data[1].replace('#','')) == 6:
                        if not all(c in string.hexdigits for c in data[1].replace('#','')):
                            approved = False
                            break

        if approved == True:
            approvedPassports += 1





print(correct)