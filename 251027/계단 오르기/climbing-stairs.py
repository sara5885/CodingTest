#251027 (21:28)
import sys
sys.setrecursionlimit(1000000)
n = int(input())
memo=[-1]*(n+1)
def stair(n):
    if memo[n]!=-1:
        return memo[n]
    if n==1:
        memo[1]=0
        return 0
    if n==2:
        memo[2]=1
        return 1
    if n==3:
        memo[3]=1
        return 1 
    memo[n]=stair(n-2)+stair(n-3)
    return memo[n]

print(stair(n)%10007)