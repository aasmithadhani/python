print("Enter 10 numbers")

with open('t1.txt','w') as f:
    for i in range(9):
        f.write(str(input("Enter number"))+'\n')
    f.write(str(input("Enter number"))+'\n')

with open('t1.txt','r') as f1,open('t2.txt','w') as f2:
    l = list()
    for i in f1:
        l.append(int(i))
    l.sort()
    for i in range(10):
        f2.write(str(l[i])+'\n')