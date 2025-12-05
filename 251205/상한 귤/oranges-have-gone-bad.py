# 251204 (16:37)
from collections import deque 
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

rotten_time=[[-2 for _ in range(n)]  for _ in range(n)]
# unvisited => -2 

# def bfs(x,y):
#     q=deque()
#     q.append((x,y))
#     while q:
#         cx,cy = q.popleft()
#         for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
#             nx,ny=cx+dx,cy+dy 
#             if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1 and rotten_time[nx][ny]==-2: #unvisited
#                 # rotten_time[nx][ny]=min(rotten_time[nx][ny],rotten_time[cx][cy]+1)
#                 rotten_time[nx][ny]=rotten_time[cx][cy]+1
#                 q.append((nx,ny))

q=deque()
for i in range(n):
    for j in range(n):
        # 상한귤 2 => rotten_time[i][j]=0 & bfs 
        # 귤 없음 0 => pass => rotten_time[i][j]=-1 
        # 귤 1 => pass 
        # 상한귤이면서 unvisited  (rotten_time[i][j]==-2)
        if grid[i][j]==0 :
            rotten_time[i][j]=-1 
        elif grid[i][j]==2:
            rotten_time[i][j]=0
            q.append((i,j))
            # bfs(i,j)

# bfs 한번에 한번만 
while q:
    cx,cy=q.popleft()
    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
        nx,ny=cx+dx,cy+dy 
        # 격자 범위 내 + 귤이 있음(1) + 아직 방문 안 함(-2)
        if 0<=nx<n and 0<=ny<n and grid[nx][ny]==1 and rotten_time[nx][ny]==-2:
            rotten_time[nx][ny] = rotten_time[cx][cy] + 1
            q.append((nx, ny))
for i in range(n):
    for j in range(n):
        print(rotten_time[i][j],end=" ")
    print()