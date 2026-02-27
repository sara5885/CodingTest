from collections import deque 
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

pq=deque()
pq.append([0,0])
visited=[[0 for _ in range(m)] for _ in range(n)]
visited[0][0]=1
while pq:
    cx,cy=pq.popleft()
    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx,ny=cx+dx,cy+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and a[nx][ny]:
            visited[nx][ny]=1
            pq.append([nx,ny])

if visited[n-1][m-1]: print(1)
else: print(0)

# for row in visited:
#     for col in row:
#         print(col,end=" ")
#     print()
