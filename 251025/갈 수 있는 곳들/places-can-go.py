from collections import deque 
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
ans=[[0]*n for _ in range(n)]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=1 
    while q:
        cx,cy=q.popleft()
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny=cx+dx,cy+dy 
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and not grid[nx][ny]:
                visited[nx][ny]=1 
                ans[nx][ny]=1 
                q.append((nx,ny))


for x,y in points:
    x,y=x-1,y-1
    visited=[[0]*n for _ in range(n)]
    visited[x][y]=1 
    ans[x][y]=1 
    bfs(x,y)

cnt=0

for row in ans:
    cnt+=sum(row)

print(cnt)