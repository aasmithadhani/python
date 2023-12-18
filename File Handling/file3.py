file_read = open('file.txt','r')
l = list()
f = file_read.read()
f = f.split(' ')
for i in f:
    l.append(str(i)[::-1])
    l.sort(key=lambda item:(item,len(item)))
print("Sorted ")
file_write = open('test2.txt','w')
for i in l:
    file_write.write(str(i)+'\n')
file_write.close()