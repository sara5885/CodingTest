# 251027 (21:45)
# import sys
# sys.setrecursionlimit(2000) 
n = int(input())
mod=1000000007


dp=[0]*(n+1)

dp[0]=1
dp[1]=2 
if n==1:
    print(2)
elif n>1:
    dp[2]=7
    for i in range(3,n+1):
        dp[i]=(3*dp[n-1]+dp[n-2]-dp[n-3]+mod)%mod

    print(dp[n])