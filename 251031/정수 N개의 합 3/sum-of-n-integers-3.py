# 251031 (13:33)
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

prefix_grid=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_grid[i][j]=prefix_grid[i-1][j]+prefix_grid[i][j-1]-prefix_grid[i-1][j-1]+arr[i-1][j-1]
ans=0
for i in range(k,n+1):
    for j in range(k,n+1):
        tmp=prefix_grid[i][j]-prefix_grid[i-k][j]-prefix_grid[i][j-k]+prefix_grid[i-k][j-k]
        if tmp>ans:
            ans=tmp
print(ans)