# 251025 (13:20)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
# 조건 + grid[x][y]>K 
safe_k,safe_cnt =0,0

max_k=1
for i in range(n):
    for j in range(m):
        if grid[i][j]>max_k:
            max_k=grid[i][j]

# 안전영역 하나에 대한 것
def dfs(k,x,y):
    visited[x][y]=1 
    for dx,dy in ((0,1),(1,0),(-1,0),(0,-1)):
        nx,ny=x+dx,y+dy 
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny]>k:
            visited[nx][ny]=1
            dfs(k,nx,ny)
    return 1 


for k in range(1,max_k):
    # 비 높이 k 일 때 안전영역개수 
    visited=[[0]*m for _ in range(n)]
    tmp_cnt=0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j]>k: #여기도 k에 대한 조건 추가해야함 
                tmp_cnt+=dfs(k,i,j)
    if tmp_cnt>safe_cnt:
        safe_cnt=tmp_cnt
        safe_k=k 

print(safe_k, safe_cnt)