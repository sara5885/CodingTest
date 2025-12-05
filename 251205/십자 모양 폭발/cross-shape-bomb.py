# 251204 (11:44)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 1. original grid update
bomb_len=grid[r-1][c-1]

sx,sy=r-1,c-1
grid[sx][sy]=0
for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
    tmp_len=1 
    cx,cy=sx,sy
    while tmp_len<bomb_len:
        nx,ny=cx+dx,cy+dy 
        tmp_len+=1
        cx,cy=nx,ny
        if 0<=nx<n and 0<=ny<n:
            grid[nx][ny]=0
            



# 2. new temp grid에 떨어진 grid 반영
temp=[[0 for _ in range(n)] for _ in range(n)]

for j in range(n):
    tmp_idx=n-1
    for i in range(n-1,-1,-1):
        if grid[i][j]!=0:
            temp[tmp_idx][j]=grid[i][j]
            tmp_idx-=1
            
            
# 3. grid=temp 
grid=temp
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()