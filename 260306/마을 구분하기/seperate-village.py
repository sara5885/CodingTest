# 260306 (15:36)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# town list : [#people]
town=[]

# 0(wall), 1(person)
visited=[[0 for _ in range(n)] for _ in range(n)]

def dfs(x,y,id):
    visited[x][y]=id
    cnt=1
    cx,cy=x,y
    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):

        nx,ny=cx+dx,cy+dy 
        if 0<=nx<n and 0<=ny<n and grid[nx][ny] and not visited[nx][ny]:
            visited[nx][ny]=id 
            cnt+= dfs(nx,ny,id)
    return cnt
cnt=1
for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            people=dfs(i,j,cnt)
            town.append(people)
            cnt+=1

# for row in visited:
#     for col in row:
#         print(col,end=" ")
#     print()


print(len(town))
town.sort()
for t in town:
    print(t)