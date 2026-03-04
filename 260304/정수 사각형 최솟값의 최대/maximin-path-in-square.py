# 260304 (17:09)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=grid[0][0]
for i in range(1,n):
    dp[0][i]=min(dp[0][i-1], grid[0][i])
    dp[i][0]=min(dp[i-1][0], grid[i][0])


for i in range(1,n):
    for j in range(1,n):
        dp[i][j]= max( min(grid[i][j],dp[i][j-1]), min(grid[i][j],dp[i-1][j]))


# for row in dp:
#     for col in row:
#         print(col,end=" ")
#     print()

print(dp[n-1][n-1])