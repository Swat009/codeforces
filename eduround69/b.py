n = int(input())
a = [int(x) for x in input().split()]
max = a[0]
maxp = 0
for i in range(n):
    if a[i]>max:
        maxp = i
        max = a[i]

i = maxp-1
j =  maxp+1
flag = 0
current = max
while i>= 0 or j<n:
    if i>=0 and j<n:
        if a[i]>a[j]:
            max = i
        else:
            max = j
        if a[max]>=current:
            flag = 1
            break
        else:
            if max == i :
                current = a[i]
                i -= 1
            else:
                current = a[j]
                j += 1
    else:
        if i>=0:
            if a[i] >= current:
                flag = 1
                break
            else:
                current = a[i]
                i -= 1
        else:
            if a[j] >= current:
                flag = 1
                break
            else:
                current = a[j]
                j += 1


if flag == 0:
    print("YES")
else:
    print("NO")