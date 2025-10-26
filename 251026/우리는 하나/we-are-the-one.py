# 251026 (18:15)
import itertools 
from collections import deque 
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# u<= grid[cx][cy]-grid[nx][ny] <=d 
cities=[]
for i in range(n):
    for j in range(n):
        cities.append((i,j))

max_city_cnt=0
selected_cities=itertools.combinations(cities,k)

# cx,cy를 기준으로 갈 수 있는 도시들 city[nx][ny]=1로 업데이트
def bfs(visited, x,y):
    global grid,u,d
    q=deque()
    q.append((x,y))
    visited[x][y]=1 
    # city[x][y]=1 

    while q:
        cx,cy=q.popleft()
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny=cx+dx,cy+dy 
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] :
                if u<=abs(grid[cx][cy]-grid[nx][ny])<=d:
                    q.append((nx,ny))
                    visited[nx][ny]=1 
                    


for cities in selected_cities:
    # possible_city=[[0 for _ in range(n)] for _ in range(n)]
    visited=[[0 for _ in range(n)] for _ in range(n)]
    city_cnt=0
    for cx,cy in cities:
        bfs(visited,cx,cy)
    
    for row in visited:
        city_cnt+=sum(row)
    max_city_cnt=max(max_city_cnt,city_cnt)
print(max_city_cnt)