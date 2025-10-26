# 251026 (15:59)
from collections import deque 
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited=[[0 for _ in range(n)] for _ in range(n) ]
pop=0
max_block=0

def dfs(x,y):
    global pop,max_block
    cnt=1 
    visited[x][y]=1 
    q=deque()
    q.append((x,y))
    while q:
        cx,cy=q.popleft()
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny=cx+dx,cy+dy 
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and grid[nx][ny]==grid[x][y]:
                cnt+=1
                visited[nx][ny]=1 
                q.append((nx,ny))
    if cnt>=4:
        pop+=1 
    if cnt>max_block:
        max_block=cnt 
    

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)

print(pop, max_block)