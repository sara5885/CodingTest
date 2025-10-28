# 251028 (18:28)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

total_max=0

def find(x,y):
    global grid 
    max_sum=0
    tmp_sum=grid[x][y]
    # case 1 : ㄱ 
    # case 2 : --- or | 
    for dx,dy in ((0,1),(0,2)):
        nx,ny=x+dx,y+dy 
        if 0<=nx<n and 0<=ny<m :
            tmp_sum+=grid[nx][ny]
    max_sum=max(max_sum,tmp_sum)
    tmp_sum=grid[x][y]

    for dx,dy in ((1,0),(2,0)):
        nx,ny=x+dx,y+dy 
        if 0<=nx<n and 0<=ny<m:
            tmp_sum+=grid[nx][ny]
    max_sum=max(max_sum,tmp_sum)
    tmp_sum=grid[x][y]

    for dx,dy in ((-1,0),(0,1)):
        nx,ny=x+dx,y+dy 
        if 0<=nx<n and 0<=ny<m:
            tmp_sum+=grid[nx][ny]
    max_sum=max(max_sum,tmp_sum)
    tmp_sum=grid[x][y]

    for dx,dy in ((-1,0),(0,-1)):
        nx,ny=x+dx,y+dy 
        if 0<=nx<n and 0<=ny<m:
            tmp_sum+=grid[nx][ny]
    max_sum=max(max_sum,tmp_sum)
    tmp_sum=grid[x][y]

    for dx,dy in ((0,-1),(1,0)):
        nx,ny=x+dx,y+dy 
        if 0<=nx<n and 0<=ny<m:
            tmp_sum+=grid[nx][ny]
    max_sum=max(max_sum,tmp_sum)
    tmp_sum=grid[x][y]

    for dx,dy in ((0,1),(1,0)):
        nx,ny=x+dx,y+dy 
        if 0<=nx<n and 0<=ny<m:
            tmp_sum+=grid[nx][ny]
    max_sum=max(max_sum,tmp_sum)
    tmp_sum=grid[x][y]

    return max_sum 

    


for i in range(n):
    for j in range(m):
        tmp_max=find(i,j)
        total_max=max(total_max,tmp_max)

print(total_max)