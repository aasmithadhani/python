
def histogram(l):
    k =[]
    x = []
    for i in range(len(l)):
        index = i
        count = 0
        for j in range(index,len(l)):
            if l[index] == l[j] and l[index] not in k:
                count+=1
            
        k = k +[l[index]]

        if count!=0:
            x+=[(l[index],count)]
        
    x.sort()
    x = sorted(x,key = lambda x:x[1])
    return x
        

print(histogram(list(map(int,input("Enter numbers").split(" ")))))