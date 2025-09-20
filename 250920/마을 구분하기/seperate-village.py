# 250920 (16:18)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 마을 array 
all_town=[]
visited=[[0]*n for _ in range(n)]

dx,dy=[-1,1,0,0],[0,0,-1,1]

def dfs(r,c):
    visited[r][c]=1
    cnt=1
    for idx in range(4):
        tmp_r,tmp_c=r+dx[idx],c+dy[idx]
        if 0<=tmp_r<n and 0<=tmp_c<n and visited[tmp_r][tmp_c]==0:
            cnt+=dfs(tmp_r,tmp_c)
    return cnt 


for i in range(n):
    for j in range(n):
        town_size=0
        if visited[i][j]==0:
            town_size=dfs(i,j)
        if town_size!=0:
            all_town.append(town_size)

print(al)

