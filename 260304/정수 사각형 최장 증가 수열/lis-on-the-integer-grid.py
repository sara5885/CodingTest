# 260304 (17:58)
import sys
sys.setrecursionlimit(10**7)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp=[[0 for _ in range(n)] for _ in range(n)]

# i,j 기준으로 상하좌우 뻗어나가면서 dp 값 업데이트 하기 
def dfs(i,j):
    if dp[i][j]!=0:
        return dp[i][j]
    
    dp[i][j]=1
    for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
        nx,ny=i+dx, j+dy 
        if 0<=nx<n and 0<=ny<n:
            if grid[nx][ny]> grid[i][j]:
                dp[i][j]=max(dp[i][j], 1+dfs(nx,ny) )

    return dp[i][j]

ans=0
for i in range(n):
    for j in range(n):
        ans=max(ans, dfs(i,j))
print(ans)

# for row in dp:
#     for col in row:
#         print(col,end=" ")
#     print()

