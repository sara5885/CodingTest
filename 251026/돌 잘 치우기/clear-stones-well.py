# 251026 (16:08)
import itertools 
import copy 
from collections import deque 
n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = [] 
all_stones=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            all_stones.append((i,j))
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# r,c array에서 k개 뽑는 조합 
stone_comb=itertools.combinations(all_stones,m)

def bfs(tmp_map,visited, r,c):
    visited[r][c]=1 
    q=deque()
    q.append((r,c))
    while q:
        cx,cy=q.popleft()
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny=cx+dx,cy+dy 
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and not tmp_map[nx][ny]:
                visited[nx][ny]=1 
                q.append((nx,ny))
max_cnt=0
for i in stone_comb:
    cnt=0
    visited=[[0 for _ in range(n)] for _ in range(n)]
    tmp_map=copy.deepcopy(grid)
    for x,y in i:
        tmp_map[x][y]=0
    for idx in range(len(r)):
        bfs(tmp_map,visited,r[idx],c[idx])
    for row in visited:
        cnt+=sum(row)
    # print(visited)
    # print(tmp_map)
    # print(cnt)
    max_cnt=max(cnt,max_cnt)

print(max_cnt)