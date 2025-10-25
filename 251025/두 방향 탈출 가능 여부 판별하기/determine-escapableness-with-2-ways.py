n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited=[[0 for _ in range(m)] for _ in range(n) ]

def dfs(x,y):
    visited[x][y]=1 
    for dx,dy in ((1,0),(0,1)):
        nx,ny=x+dx,y+dy 
        if  0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny] :
            visited[nx][ny]=1 
            dfs(nx,ny)

dfs(0,0)
if visited[n-1][m-1]==1:
    print(1)
else:
    print(0)
