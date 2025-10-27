# 251027 (23:17)
import sys 
INT_MAX=sys.maxsize
M, N = map(int, input().split())
coin = list(map(int, input().split()))

# 최소동전수 
dp=[INT_MAX]*(N+1)
for i in range(M):
    dp[coin[i]]=1
for i in range(1,N+1):
    for j in range(M):
        if i>coin[j]:
            # if dp[i-coin[j]]==INT_MAX:
            #     continue 
            dp[i]=min(dp[i-coin[j]]+1, dp[i])

# print(dp)
if dp[N]==INT_MAX:
    print(-1)
else:
    print(dp[N])