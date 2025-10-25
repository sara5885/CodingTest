from collections import deque 
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1 

    while q:
        cx,cy=q.popleft()
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny=cx+dx,cy+dy 
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and a[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
bfs(0,0)
if visited[n-1][m-1]:
    print(1)
else:
    print(0)
