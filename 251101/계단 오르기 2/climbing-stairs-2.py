#251101 (18:11)
import sys 
INT_MIN=-sys.maxsize 
n = int(input())
coin = [0] + list(map(int, input().split()))

# 3번 1계단? 
# dp[i][j] : i층높이의 계단에 있고 1계단으로 j번올라간 상황 

dp=[[INT_MIN for _ in range(4)] for _ in range(n+1)]
dp[0][0]=0
dp[1][0]=0
dp[1][1]=coin[1]

for i in range(1,n+1):
    for j in range(1,4):
        dp[i][j]=max(dp[i-2][j]+coin[i], dp[i-1][j-1]+coin[i])
# for i in range(1,n+1):
#     for j in range(1,4):
#         print(dp[i][j], end=" ")
#     print()
# print()
print(dp[n][3])
