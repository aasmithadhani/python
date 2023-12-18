fileread = open('file.txt','r')
l = list()
f = fileread.read()
f = f.split(' ')
for line in f:
    l.append(str(line))
    l.sort(key=lambda item: (item,len(item)))
print("sorted in lexographical order")
filewrite = open('test1.txt','w')
for i in l:
    filewrite.write(str(i)+'\n')
filewrite.close()