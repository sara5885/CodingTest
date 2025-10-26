# 250923 (01:00)
from collections import deque 
n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

s_pos=[] #what's this 

for _ in range(k):
    r, c = tuple(map(int, input().split()))
    s_pos.append((r - 1, c - 1))


stone_pos=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            stone_pos.append([i,j])

selected_stones=[]

# for dfs 
q=deque() # global variable 
# q에는 x,y 좌표가 들어감 

visited=[[0]*n for _ in range(n)]
max_cnt=0

def in_range(x,y):
    return 0<=x<n and 0<=y<n 
def can_go(x,y):
    return in_ranage(x,y) and not a[x][y] and visited[x][y]==0 
dx,dy=[-1,1,0,0],[0,0,-1,1]
def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            tmp_x,tmp_y=x+dx[i],y+dy[i]
            if can_go(tmp_x,tmp_y):
                q.append(tmp_x,tmp_y)
                visited[tmp_x][tmp_y]=1 

def calc():


# backtracking 
def find_max(idx,cnt):
    global ans 
    if idx==len(stone_pos):
        if cnt==m:
            ans=max(ans,calc())
        return 
    selected_stones.append(stone_pos[idx])




find_max(0,0)
print(ans)
