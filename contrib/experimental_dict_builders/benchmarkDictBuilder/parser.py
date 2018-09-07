import csv

def loadFile(filename):
    file = open(filename, 'r')
    content = file.readlines()
    file.close()
    return content

def writeFile(filename, table):
    with open(filename, 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        for list in table:
            spamwriter.writerow(list)

def getMiddleString(s, front, back):
    res = s.split(front)
    res1 = res[1].split(back)
    return res1[0]

if __name__ == "__main__":
    content = loadFile("merge.txt")
    time = "none"
    name = "none"
    f = ""
    a = ""
    d = ""
    k = ""
    ratio = ""
    count = 0
    minimum = 100
    table = []
    headers = ["dictionary", "f", "a", "time", "ratio", "d", "k"]
    table.append(headers)
    firstcover = 1
    num = 0
    for line in content:
        if "took" in line:
            res = line.split("took ")
            res2 = res[0].split(" ")
            name = res2[0]
            res1 = res[1].split(" seconds")
            time = res1[0]
        if "current f is " in line:
            count = 0
            f = getMiddleString(line, "current f is ", "\n")
        if "current accel is " in line:
            a = getMiddleString(line, "current accel is ", "\n")
        if "k=" in line:
            k = getMiddleString(line, "k=", "\n")
        if "d=" in line:
            d = getMiddleString(line, "d=", "\n")
            if name == "COVER":
                print(name + f + "       " + time + "       " + ratio + "        " + d + "          " + k)
                list = []
                if firstcover == 1:
                    list = [name+"(opt)", "", "", time, ratio, d, k]
                    firstcover = 0
                else:
                    list = [name, "", "", time, ratio, d, k]
                    firstcover = 1
                table.append(list)
            else:
                name = "FASTCOVER"
                if count == 0:
                    print(name + " f=" + f + " a=" + a + "       " + time + "       " + ratio + "        " + d + "          " + k)
                    list = [name+"(opt)", f, a, time, ratio, d, k]
                    table.append(list)
                    count += 1
                else:
                    if float(time) < minimum:
                        minimum = float(time)
                    if count == 5:
                        print(name + " f=" + f + " a=" + a + "       " + str(minimum) + "       " + ratio + "        " + d + "          " + k)
                        list = [name, f, a, time, ratio, d, k]
                        table.append(list)
                        count = 0
                        minimum = 100
                    else:
                        count += 1
        if "dictionary is " in line:
            ratio = getMiddleString(line, "dictionary is ", "\n")
            if name == "RANDOM" or name == "NODICT" or name == "LEGACY":
                list = [name, "", "", time, ratio, "", ""]
                table.append(list)
                print(name + f + "       " + time + "       " + ratio + "        ")
        if "-----" in line:
            print("----")
            csvname = "res"+str(num)+".csv"
            num += 1
            writeFile(csvname, table)
            table = []
            table.append(headers)
            f = ""
