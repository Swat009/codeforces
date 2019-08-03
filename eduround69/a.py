t = int(input())

while t>0:
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    m1 = a[0]
    m2 = a[1]
    i = n-3
    flag = 0
    while i>=0:
        if(m1>=(i+2) and m2>=(i+2)):
            print(i+1)
            flag = 1
            break
        i -= 1
    if flag == 0:
        print(0)
    t -= 1

