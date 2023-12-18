def hanoi(n,src,aux,target):
    if n==1:
        print(f'Move disk 1 from peg {src} to peg {target}')
        return
    hanoi(n - 1, src, target, aux)
    print("Move disk {} from peg {} to peg {}".format(n, src, target))
    hanoi(n - 1, aux, src, target)



n = int(input("No of disks: "))
hanoi(n,'A','B','C')
