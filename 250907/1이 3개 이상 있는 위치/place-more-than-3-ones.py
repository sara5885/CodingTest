n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx,dy=[0,1,0,-1],[1,0,-1,0]
cnt=0
def is_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for i in range(n):
    for j in range(n):
        # i,j 
        tmp_cnt=0
        for k in range(4):
            nx,ny=i+dx[k],j+dy[k]
            if is_range(nx,ny) and grid[nx][ny]==1:
                tmp_cnt+=1
        if tmp_cnt>=3:
            cnt+=1

print(cnt)
