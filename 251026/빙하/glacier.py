from collections import deque 
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# bfs 사용 
remained_ice=0
for row in a:
    remained_ice+=sum(row)
ice_size=0

def bfs(i,j):
    visited=[[0 for _ in range(m)] for _ in range(n)]
    visited[i][j]=1 
    q=deque()
    q.append((i,j))
    while q:
        cx,cy=q.popleft()
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny=dx+cx,dy+cy 
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny]=1
                if a[nx][ny]:
                    a[nx][ny]=0
                else:
                    q.append((nx,ny))
cnt=0
while remained_ice:
    cnt+=1
    ice_size=remained_ice
    bfs(0,0)
    remained_ice=0
    for row in a:
        remained_ice+=sum(row)

print(cnt,ice_size)