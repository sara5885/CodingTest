# 250917 (10:38)
# bfs() : 큐를 비울 때까지 꺼내고, 인접 노드를 확인해서 조건 맞으면 push
from collections import deque 
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited=[[0]*m for _ in range(n)]
step=[[0]*m for _ in range(n)]

dx,dy=[1,0,-1,0],[0,1,0,-1]

def bfs():
    # initialization 
    # 시작 칸이 막혀있으면 탐색 불가
    if a[0][0] != 1:
        return
    q=deque()
    q.append((0,0))
    step[0][0]=0
    visited[0][0]=1
    while q:
        # pop 
        x,y=q.popleft()
        for i in range(4):
            tmp_x,tmp_y=x+dx[i], y+dy[i]
            if 0<=tmp_x<n and 0<=tmp_y<m and a[tmp_x][tmp_y]==1 and visited[tmp_x][tmp_y]==0:
                step[tmp_x][tmp_y]=step[x][y]+1
                q.append((tmp_x,tmp_y))
                visited[tmp_x][tmp_y]=1 

bfs()
if visited[n-1][m-1]==0:
    print(-1)
else:
    print(step[n-1][m-1])