n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited=[[0]*n for _ in range(n)]

town_arr=[]

def dfs(x,y):
    cnt=1
    visited[x][y]=1
    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
        nx,ny=x+dx,y+dy 
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and grid[nx][ny]:
            cnt+=dfs(nx,ny)
    return cnt

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            town_size=dfs(i,j)
            if town_size:
                town_arr.append(town_size)

print(len(town_arr))
town_arr.sort()
for i in town_arr:
    print(i)