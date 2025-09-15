# 250915 (12:47)
from collections import deque 
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

dx,dy=[1,0,-1,0],[0,1,0,-1]

total_visited=[
    [0]*(n+1) for _ in range(n+1)]

for i in range(k):
    visited=[[0]*(n+1)for _ in range(n+1)]
    x,y=points[i]
    q=deque([(x,y)])
    visited[x][y]=1

    while q:
        x,y=q.popleft()
        for j in range(4):
            tmp_x,tmp_y=x+dx[j], y+dy[j]
            if tmp_x>=1 and tmp_x<=n and tmp_y>=1 and tmp_y<=n and visited[tmp_x][tmp_y]==0 and grid[tmp_x-1][tmp_y-1]==0:
                visited[tmp_x][tmp_y]=1
            
                q.append((tmp_x,tmp_y))
    for a in range(n+1):
        for b in range(n+1):
            if visited[a][b]==1:
                total_visited[a][b]=1

        for b in range(n+1):
            if visited[a][b]==1:
                total_visited[a][b]=1

tmp_sum=0
for col in total_visited:
    tmp_sum+=sum(col)

print(tmp_sum)




        
