# 251026 (17:09)
import copy 
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

melting_t=0
ice_size=0

remained_ice=0
for row in a:
    remained_ice+=sum(row)
while remained_ice: #빙하남아있을때 

    melting_t+=1
    ice_size=remained_ice
    visited=[[0 for _ in range(m)] for _ in range(n)]
    tmp_grid=copy.deepcopy(a)
    for cx in range(n):
        for cy in range(m): 
            if not a[cx][cy]:#물이라면 주변 빙하 녹이기 
                melting_check=False
                for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)): #주변 0 하나라도 있나 확인 
                    nx,ny=cx+dx,cy+dy 
                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and not a[nx][ny]:
                        melting_check=True 
                if melting_check:
                    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                        nx,ny=cx+dx,cy+dy 
                        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and a[nx][ny]:
                            tmp_grid[nx][ny]=0
                            visited[nx][ny]=1
    a=tmp_grid
    remained_ice=0
    for row in a:
        remained_ice+=sum(row)

    # for row in a:
    #     for col in row:
    #         print(col,end=" ")
    #     print()
                        
print(melting_t, ice_size)