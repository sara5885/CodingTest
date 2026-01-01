# 251121 (11:26)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


dx,dy=[-1,-1,1,1],[1,-1,-1,1]
# if out ouf index -> idx+=1 

idx=0
ans=0
for i in range(n):
    for j in range(n):
        tmp=grid[i][j]
        cx,cy=i,j 
        for dx,dy in ((-1,1),(-1,-1),(1,-1),(1,1)):
            nx,ny=cx+dx, cy+dy 
            if (nx,ny)==(i,j):
                continue
            while 0<=nx<n and 0<=ny<n :
                if i==2 and j==1:
                    print(grid[nx][ny],end=" ")
                tmp+=grid[nx][ny]
                nx,ny=nx+dx,ny+dy 
        ans=max(ans,tmp)

print(ans)