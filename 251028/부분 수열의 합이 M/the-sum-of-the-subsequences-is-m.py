n, m = map(int, input().split())
A = list(map(int, input().split()))

dp=[101]*(m+1)
dp[0]=0 
for i in range(n):
    for j in range(m,-1,-1):
        if dp[j-A[i]]!=101:
            dp[j]=min(dp[j], dp[j-A[i]]+1)

if dp[m]==101:
    print(-1)
else:
    print(dp[m])