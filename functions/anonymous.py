list1 = list(map(int,input("Enter elements for list 1: ").split(" ")))
list2 = list(map(int,input("Enter elements for list 2: ").split(" ")))

result = list(map(lambda a,b:a+b,list1,list2))
print(f'addition is {result}')

arr = list(map(int,input("Enter elements").split(" ")))
result = list(map(lambda x:x**3,filter(lambda x:x%2!=0,arr)))
print(result)

