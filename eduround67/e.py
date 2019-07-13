"""
Tried editorial approach but was not able to pass all test cases even on increaseing the recursion limit.
Fails on test 33
"""
from sys import setrecursionlimit
import sys
sys.setrecursionlimit(int(1e9))
ans = 0
def calcsize(node, size, p=-1):
    size[node] += 1
    for v in E[node]:
        if p == v:
            continue
        size[node] += calcsize(v,size,node)
    return size[node]

def calcdp(node, size, dp, p=-1):
    dp[node] += size[node]
    for v in E[node]:
        if p==v:
            continue
        dp[node] += calcdp(v,size,dp,node)
    return dp[node]

def dfs(node, size, dp,  p=-1):
    global ans
    ans = max(ans,dp[node])
    for v in E[node]:
        if p == v:
            continue
        size[node] -= size[v]
        dp[node] -= size[v]
        dp[node] -= dp[v]
        dp[v] += size[node]
        dp[v] += dp[node]
        size[v] += size[node]
        dfs(v,size,dp,node)
        size[v] -= size[node]
        dp[v] -= size[node]
        dp[v] -= dp[node]
        dp[node] += size[v]
        dp[node] += dp[v]
        size[node] += size[v]
    return ans

n = int(input())
E = [ [] for i in range(n)]
size = [0]*n
dp = [0]*n
for i in range(n-1):
    u,v = map(int,input().split())
    u = u-1
    v = v-1
    E[u].append(v)
    E[v].append(u)

calcsize(0,size)
calcdp(0,size,dp)
dfs(0,size,dp)
print(ans)



