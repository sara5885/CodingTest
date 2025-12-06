
n = int(input())

# Please write your code here.
dp=[[0 for _ in range(10)] for _ in range(n+1)]
for i in range(1,n+1):
    dp[0][i]=1 
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=dp[i-1][j-1] + dp[i-1][j+1]
