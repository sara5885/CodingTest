# 250917 (10:55)
from collections import deque 
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx,dy=[-2,-2,-1,-1,1,1,2,2],[-1,1,-2,2,-2,2,-1,1]
step=[[0]*n for _ in range(n)]

def bfs():
    q=deque([(r1-1,c1-1)])
    step[r1-1][c1-1]=0
    
    while q:
        x,y=q.popleft()
        
        for i in range(8):
            tmp_x,tmp_y=x+dx[i],y+dy[i]
            if 0<=tmp_x<n and 0<=tmp_y<n and step[tmp_x][tmp_y]==0:
                step[tmp_x][tmp_y]=step[x][y]+1
                q.append((tmp_x,tmp_y))

bfs()

if step[r2-1][c2-1]==0:
    print(-1)
else:
    print(step[r2-1][c2-1])
