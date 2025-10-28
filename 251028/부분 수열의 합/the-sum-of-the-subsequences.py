#251028 (20:45)

n, m = map(int, input().split())
A = list(map(int, input().split()))

# dp[i]: 부분수열의 합으로 i만들기 가능한지 
# dp[i] : 
# if dp[i-A[j]] == 1 : dp[i]=1 
dp=[-1]*(m+1)
dp[0]=1
for i in range(n):
    for j in range(m,-1,-1):
        if j>=A[i] and dp[j-A[i]]!=-1:
            dp[j]=1 

# print(dp[m])
if dp[m]==1:
    print('Yes')
else:
    print('No')