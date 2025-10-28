# 251028 (20:23) (20:)
N, M = map(int, input().split())
coin = list(map(int, input().split()))

# max coin 
# dp[i]: 금액 i를 만드는 동전의 최대 개수 
# for j in range(M)
    # if i>=coin[j]:
        #dp[i]=max(dp[i-coin[j]]+1, dp[i])
dp=[-1]*(M+1)
dp[0]=0
for i in range(M+1):
    for j in range(N):
        if i>=coin[j] and dp[i-coin[j]]!=-1:
            dp[i]=max(dp[i], dp[i-coin[j]]+1)

if dp[M]==0:
    print(-1)
else:
    print(dp[M])