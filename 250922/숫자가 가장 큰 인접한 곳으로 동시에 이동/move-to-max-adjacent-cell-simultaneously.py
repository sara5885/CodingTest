#250922 (03:42)
n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0]-1 for pos in marbles]
c = [pos[1]-1 for pos in marbles]

grid=[[0]*(n) for _ in range(n)]
for i in range(m):
    grid[r[i]][c[i]]=1

dx,dy=[-1,1,0,0],[0,0,-1,1]

for sec in range(t):
    new_grid=[[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                continue 
            else:
                tmp_max=0 
                tmp_max_x=-1
                tmp_max_y=-1
                for k in range(4):
                    tmp_x,tmp_y=i+dx[k],j+dy[k]
                    if 0<=tmp_x<n and 0<=tmp_y<n:
                        if a[tmp_x][tmp_y]>tmp_max:
                            tmp_max=a[tmp_x][tmp_y]
                            tmp_max_x=tmp_x
                            tmp_max_y=tmp_y
         
                if new_grid[tmp_max_x][tmp_max_y]==1:
                    new_grid[tmp_max_x][tmp_max_y]=0
                else:
                    new_grid[tmp_max_x][tmp_max_y]=1
                            
    grid=[r[:] for r in new_grid]

ans=0
for row in grid:
    ans+=sum(row)
print(ans)