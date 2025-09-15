# 250915 (13:29)

# max_num을 현재 시점부터 비교하는 것 X 
from collections import deque 
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
x,y=r-1,c-1
# max_visited=[[0]*(n+1)for _ in range(n+1)]
dx,dy=[1,0,-1,0],[0,1,0,-1]

s_x,s_y =x,y 
for i in range(k):
    # start point 존재 
    # start point -> bfs 진행 
    # bfs : 진행하면서 max point, max update 진행 
    # start num, start point 설정 
    start_val=grid[s_x][s_y]
    visited=[[0]*(n)for _ in range(n)]
    q=deque([(s_x,s_y)]) #i마다 새로운 queue (max num, max point는 따로 저장)
    max_pos=None  
    max_num=0
    while q: 
        x,y=q.popleft()
        visited[x][y]=1 

        for j in range(4):
            tmp_x,tmp_y=x+dx[j],y+dy[j]
            if 0<=tmp_x<n and 0<=tmp_y<n and grid[tmp_x][tmp_y]<start_val and visited[tmp_x][tmp_y]==0:
                # 1. q에 추가 
                visited[tmp_x][tmp_y]=1
                q.append((tmp_x,tmp_y))
                # 2. max point, num update 
                if grid[tmp_x][tmp_y]>max_num:
                    max_num=grid[tmp_x][tmp_y]
                    max_pos=(tmp_x,tmp_y)
                elif grid[tmp_x][tmp_y]==max_num and (max_pos is None or (tmp_x,tmp_y)<max_pos):
                        max_pos=(tmp_x,tmp_y) 
                        
    if max_pos is None:
        break
    s_x,s_y=max_pos

print(s_x+1,s_y+1)