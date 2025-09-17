# 250917 (11:03 )
from collections import deque 
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer=[[0]*n for _ in range(n)]

# 0 : 이동가능 
# 1 : 이동 X
# 2 : 칸에 사람 있음 
# 3 : 비를 피할 수 있음 

dx,dy=[1,-1,0,0],[0,0,1,-1]

# h번 (r1,c1 -> r2,c2)
# people list 만들기 
src_list=[]
dst_list=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            src_list.append((i,j))
        elif grid[i][j]==3:
            dst_list.append((i,j))

# 한사람에 대한 bfs 인것 

def bfs(r1,c1):
    step=[[0]*n for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    q=deque()
    q.append((r1,c1))
    step[r1][c1]=0

    while q:
        x,y=q.popleft()
        # print('x,y:',x,y)
        # print('q:',q)
        for i in range(4):
            tmp_x,tmp_y=x+dx[i],y+dy[i]
            # print('tmp_x,tmp_y:',tmp_x,tmp_y)
            if 0<=tmp_x<n and 0<=tmp_y<n and visited[tmp_x][tmp_y]==0:
                visited[tmp_x][tmp_y]=1
                if grid[tmp_x][tmp_y]==0 or grid[tmp_x][tmp_y] ==2:
                    
                    q.append((tmp_x,tmp_y))
                    step[tmp_x][tmp_y]=step[x][y]+1 
                elif grid[tmp_x][tmp_y]==3:
                    # print('DEBUGGING2')
                    # print('grid[tmp_x][tmp_y]==3 / step[x][y]+1:',tmp_x,tmp_y,step[x][y]+1)
                    return step[x][y]+1

    return -1 



for i in range(len(src_list)):
    r,c=src_list[i]
    answer[r][c]=bfs(r,c)

for row in answer:
    for col in row :
        print(col,end=" ")
    print()