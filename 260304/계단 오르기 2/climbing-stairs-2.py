# # 260304 (21:10)
# import sys 
# INT_MIN=-sys.maxsize 
# n = int(input())
# # coin = [0] + list(map(int, input().split()))
# coin = list(map(int, input().split()))
# # Please write your code here.
# dp=[[INT_MIN for _ in range(4)] for _ in range(n)]
# dp[0][1]=coin[0]

# for i in range(1,n):
#     for j in range(1,4):
#         # dp[i][j]=max(dp[i-1][j-1]+coin[i], dp[i-2][j-1]+coin[i], dp[i-1][j], dp[i-2][j])
#         # dp[i][j]=max(dp[i-1][j-1]+coin[i], dp[i-2][j]+coin[i])
#         # 1칸 이동
#         if j > 0:
#             dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coin[i])

#         # 2칸 이동
#         if i >= 2:
#             dp[i][j] = max(dp[i][j], dp[i-2][j] + coin[i])

# # print(max(dp[-1]))

# for row in dp:
#     for col in row:
#         print(col,end=" ")
#     print()

import sys
INT_MIN = -sys.maxsize

n = int(input())
coin = list(map(int, input().split()))

dp = [[INT_MIN]*4 for _ in range(n)]

# 시작 이동
dp[0][1] = coin[0]
if n > 1:
    dp[1][0] = coin[1]

for i in range(n):
    for j in range(4):

        # 1칸 이동
        if i >= 1 and j >= 1 and dp[i-1][j-1] != INT_MIN:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coin[i])

        # 2칸 이동
        if i >= 2 and dp[i-2][j] != INT_MIN:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coin[i])

print(max(dp[n-1]))