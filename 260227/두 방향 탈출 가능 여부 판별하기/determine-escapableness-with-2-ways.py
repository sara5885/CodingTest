n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited=[[0 for _ in range(m+1)] for _ in range(n+1)]

def dfs(i,j):
    visited[i][j]=1 
    for dx,dy in ((1,0), (0,1)):
        nx,ny=i+dx,j+dy 
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny]:
            dfs(nx,ny)

dfs(0,0)
if visited[n-1][m-1]: print(1)
else: print(0)
