# 260304 (21:10)
import sys 
INT_MIN=-sys.maxsize 
n = int(input())
# coin = [0] + list(map(int, input().split()))
coin = list(map(int, input().split()))
# Please write your code here.
dp=[[INT_MIN for _ in range(4)] for _ in range(n)]
for i in range(n):
    dp[i][0]=0
dp[0][1]=coin[0]

for i in range(n):
    for j in range(1,4):
        # dp[i][j]=max(dp[i-1][j-1]+coin[i], dp[i-2][j-1]+coin[i], dp[i-1][j], dp[i-2][j])
        dp[i][j]=max(dp[i-1][j-1]+coin[i], dp[i-2][j]+coin[i])

print(max(dp[-1]))