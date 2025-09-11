n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
# nx,ny=n//2,n//2 
# idx=0
# dx,dy=[0,-1,0,1],[1,0,-1,0]

# for i in range(1,n*n+1):
#     grid[nx][ny]=i 
#     tmp_x,tmp_y=nx+dx[idx],ny+dy[idx]
#     if tmp_x<0 or tmp_y<0 or tmp_x>=n or tmp_y>=n 

nx,ny=n-1,n-1 
idx=0 
dx,dy=[0,-1,0,1],[-1,0,1,0]
for i in range(n*n,0,-1):
    # print(i,nx,ny)
    grid[nx][ny]=i 
    tmp_x,tmp_y=nx+dx[idx],ny+dy[idx]
    if tmp_x<0 or tmp_y<0 or tmp_x>=n or tmp_y>=n or grid[tmp_x][tmp_y]!=0:
        idx=(idx+1)%4 
    nx,ny=nx+dx[idx],ny+dy[idx]

for row in grid:
    for col in row:
        print(col,end=" ")
    print('')

