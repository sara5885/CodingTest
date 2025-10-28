#251028 (19:26)
n, m = map(int, input().split())
A = list(map(int, input().split()))

dp=[101]*(m+1)
dp[0]=0

for i in range(n): # 수열 길이 (수열 idx)
    for j in range(m,-1,-1): # 총 합 
        if j>=A[i]:
            if dp[j-A[i]]==101:
                continue 
            dp[j]=min(dp[j], dp[j-A[i]]+1)
ans=dp[m]
if ans==101:
    ans=-1 
print(ans)

