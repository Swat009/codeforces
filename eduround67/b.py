n = int(input())
s = input()

map = {}

for i in range(len(s)):
    key = ord(s[i]) - ord('a')
    if key in map:
        map[key].append(i)
    else:
        map[key] = [i]

m = int(input())
while m>0:
    t = input()
    tmap = {}
    for i in range(len(t)):
        key = ord(t[i]) - ord('a')
        if key in tmap:
            tmap[key] += 1
        else:
            tmap[key] = 1
    maxv =0
    for key, value in tmap.items():
            lis = map[key]
            mv = lis[value-1]
            maxv = max(maxv, mv)
    print(maxv+1)
    m -= 1