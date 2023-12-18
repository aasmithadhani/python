#Factorial
# num = int(input("Enter number"))
# result =1
# for i in range(1,num+1):
#     result*=i
# if num == 0:
#     result=1

# print("RESULT: ",str(result))
    
#Fibonacci series
n = int(input("Enter no"))
a = 0
b =1
if n == 1:
    print(a)
elif n>=2:
    print(a)
    print(b)
    for i in range(n-2):
        c = a+b
        a = b
        b=c
        print(c)


y = int(input("Enter year: "))

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(y, "is a leap year.")
        else:
            print(y, "is not a leap year.")
    else:
        print(y, "is a leap year.")   
else:
    print(y, "is not a leap year.")    
