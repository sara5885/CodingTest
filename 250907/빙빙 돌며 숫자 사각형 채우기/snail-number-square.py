n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

grid=[
    [
        0 for _ in range(m)
    ]
    for _ in range(n)
]
# dir0(->) : (0,1)
# dir1(아래) : (1,0)
# dir2(<-) : (0,-1)
# dir3(위) : (-1,0)
dx,dy=[0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

now_dir=0
n_dx,n_dy=0,0
grid[n_dx][n_dy]=1
for i in range(2,n*m+1):
    t_dx,t_dy=n_dx+dx[now_dir],n_dy+dy[now_dir]
    if in_range(t_dx,t_dy) and grid[t_dx][t_dy]==0:
        n_dx,n_dy=n_dx+dx[now_dir],n_dy+dy[now_dir]
        grid[n_dx][n_dy]=i
    else: #change direction
        now_dir=(now_dir+1)%4
        n_dx,n_dy=n_dx+dx[now_dir],n_dy+dy[now_dir]
        grid[n_dx][n_dy]=i

for row in grid:
    for col in row:
        print(col,end=" ")
    print('')