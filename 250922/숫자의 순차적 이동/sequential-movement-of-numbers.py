# 250922 (15:01) (15:12)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx,dy=[-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1]
for t in range(m):# turn
    value=1 
    while value<=n*n:
        for i in range(n):
            for j in range(n):
                if grid[i][j]!=value:
                    continue
                else:
                    # find max 
                    tmp_max=-1
                    tmp_max_r=-1
                    tmp_max_c=-1
                    for k in range(8):
                        tmp_r,tmp_c=i+dx[k],j+dy[k]
                        if 0<=tmp_r<n and 0<=tmp_c<n:
                            if grid[tmp_r][tmp_c]>tmp_max:
                                tmp_max=grid[tmp_r][tmp_c]
                                tmp_max_r=tmp_r
                                tmp_max_c=tmp_c
                    grid[tmp_max_r][tmp_max_c]=grid[i][j]
                    grid[i][j]=tmp_max
                value+=1
        # print(grid)


for row in grid:
    print(*row)