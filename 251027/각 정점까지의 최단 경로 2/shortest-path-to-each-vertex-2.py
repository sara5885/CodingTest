# 251027 (23:30)
import sys 
INT_MAX=10000000
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

grid=[[INT_MAX for _ in range(n)] for _ in range(n)]
for i in range(n):
    grid[i][i]=0

for i,j,w in edges:
    grid[i-1][j-1]=min(grid[i-1][j-1],w)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if grid[i][k]==INT_MAX or grid[k][j]==INT_MAX:
                continue
            if grid[i][j]>grid[i][k]+grid[k][j]:
                grid[i][j]=grid[i][k]+grid[k][j]

for row in grid:
    for col in row:
        if col==INT_MAX:
            print(-1,end=" ")
        else:
            print(col,end=" ")
    print()