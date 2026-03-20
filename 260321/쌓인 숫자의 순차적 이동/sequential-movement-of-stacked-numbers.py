# 260320 (18:17)
from collections import deque 
n, m = map(int, input().split())
tmp_arr = [list(map(int, input().split())) for _ in range(n)]
move_nums = list(map(int, input().split()))
# union-find 
parent=list(range(n*n+1))
grid=[[[]for _ in range(n)] for _ in range(n)]
# 해당 숫자가 현재 어느 좌표에 있는지 
loc=dict()
for i in range(n):
    for j in range(n):
        loc[tmp_arr[i][j]]=(i,j)
        grid[i][j].append(tmp_arr[i][j])

for num in move_nums:
    # print("num:",num)
    cx,cy = loc[num]
    mx,my,mw=-1,-1,0

    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
        nx,ny = cx+dx, cy+dy 
        
        if 0<=nx<n and 0<=ny<n: # and grid[nx][ny]:
            # for tmp in grid[nx][ny]:
            for idx in range(len(grid[nx][ny])):
                if grid[nx][ny][idx] > mw :
                    mw=grid[nx][ny][idx]
                    mx,my = nx,ny 

    if (mx,my)!=(-1,-1):

        n_idx=grid[cx][cy].index(num)
        for tmp_n in grid[cx][cy][n_idx:]:
            loc[tmp_n]=mx,my
        grid[mx][my]+=grid[cx][cy][n_idx:]
        del grid[cx][cy][n_idx:]


for i in range(n):
    for j in range(n):
        if len(grid[i][j])==0:
            print("None")
        else:
            tmp=grid[i][j][::-1]
            
            for d in tmp:
                print(d,end=" ")
            print()
