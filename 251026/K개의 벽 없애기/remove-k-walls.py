# 251026 (18:40)
import itertools 
import copy 
from collections import deque 
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

wall=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            wall.append((i,j))

remove_walls=itertools.combinations(wall, k)
min_dist=101
def bfs(visited,tmp_grid,x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=0

    while q:
        cx,cy=q.popleft()
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny=dx+cx,dy+cy 
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1 and not tmp_grid[nx][ny]:
                visited[nx][ny]=visited[cx][cy]+1
                q.append((nx,ny))


for walls in remove_walls:
    visited=[[-1 for _ in range(n)] for _ in range(n)]
    tmp_dist=0
    # walls: 없앨 wall의 좌표들 존재 
    tmp_grid=copy.deepcopy(grid)
    for i,j in walls:
        tmp_grid[i][j]=0 
    bfs(visited,tmp_grid,r1,c1)
    if visited[r2][c2]!=-1:
        min_dist=min(min_dist,visited[r2][c2])

    # for row in visited:
    #     for col in row:
    #         print(col,end=" ")
    #     print()
if min_dist==101:
    print(-1)
else:
    print(min_dist)