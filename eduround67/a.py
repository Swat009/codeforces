t = int(input())

while t>0:
    n,st,tt = [int(v) for v in input().split()]
    nost = n-st
    nott = n-tt
    minno = max(nost,nott)+1
    print(minno)
    t -= 1