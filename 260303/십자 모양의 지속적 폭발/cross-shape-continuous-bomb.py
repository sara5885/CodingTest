#260303 (16:37)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

for c in commands : 
    # c : 현재 column 
    c-=1
    row=-1
    for i in range(n):
        if grid[i][c]!=0:
            row=i 
            break 
    if row==-1: continue 

    bomb=grid[row][c]
    new_grid=grid.copy()
    new_grid[row][c]=0
    # print(bomb)
    if bomb>=2:
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            cx,cy=row,c
            for b in range(bomb-1):
                nx,ny=cx+dx, cy+dy 
                if 0<=nx<n and 0<=ny<n :
                    new_grid[nx][ny]=0
                    cx,cy=nx,ny
    # for i in new_grid:
    #     for j in i:
    #         print(j,end=" ")
    #     print()
    # print('----')
    new_new_grid=[[0 for _ in range(n)] for _ in range(n)]
    
    for j in range(n): #column
        piv=n-1
        for i in range(n-1,-1,-1):
            if new_new_grid[piv][j]==0:
                new_new_grid[piv][j]=new_grid[i][j]
            else:
                piv-=1
                new_new_grid[piv][j]=new_grid[i][j]
    grid=new_new_grid 
    
for i in grid:
    for j in i :
        print(j,end=" ")
    print()


