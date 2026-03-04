# 260304 (19:40)
import sys 
INT_MIN=-sys.maxsize
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp=[[INT_MIN for _ in range(m)] for _ in range(n)]

dp[0][0]=1 
for i in range(1,n):
    for j in range(1,m):
        for k in range(0,i):
            for l in range(0,j):
                if grid[i][j]>grid[k][l]:
                    dp[i][j]=max(dp[i][j], dp[k][l]+1)

ans=0
for row in dp:
    ans=max(ans, max(row))
print(ans)

