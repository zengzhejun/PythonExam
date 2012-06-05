file1 = open("c:\\aa.txt")
line = file1.readline()
while line:
    print(line)
    line = file1.readline()
    print(line)
file1.close()