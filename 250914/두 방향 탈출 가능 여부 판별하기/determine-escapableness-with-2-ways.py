# 250914 (17:54) (18)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


# start : 0,0 
dx,dy=[1,0],[0,1]
visited=[
    [
        0 for _ in range(m)
    ]
    for _ in range(n)
]

def dfs(x,y):
    visited[x][y]=1
    for i in range(2):
        tmp_x,tmp_y=x+dx[i], y+dy[i]
        if tmp_x>=0 and tmp_x<n and tmp_y>=0 and tmp_y<m and grid[tmp_x][tmp_y]==1  and visited[tmp_x][tmp_y]==0:
            visited[tmp_x][tmp_y]=1
            # print(visited)
            dfs(tmp_x,tmp_y)
dfs(0,0)

if visited[n-1][m-1]==1:
    print(1)
else:
    print(0)
