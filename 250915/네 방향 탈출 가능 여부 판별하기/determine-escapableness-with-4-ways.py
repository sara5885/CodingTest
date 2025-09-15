# 250915 (12:25)
from collections import deque 
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx,dy=[1,0,-1,0],[0,1,0,-1]

visited=[
    [0 for _ in range(m)]
    for _ in range(n)
]


def bfs():
    # first element queue에 넣어주기 

    n_x,n_y=0,0
    visited[n_x][n_y]=1
    q=deque([(n_x,n_y)])

    while q:
        n_x,n_y=q.popleft()
        # ### 처리

        for i in range(4):
            tmp_x,tmp_y=n_x+dx[i], n_y+dy[i]
            if tmp_x >=0 and tmp_x< n and tmp_y>=0 and tmp_y<m and a[tmp_x][tmp_y]==1 and visited[tmp_x][tmp_y]==0:
                visited[tmp_x][tmp_y]=1
                q.append((tmp_x,tmp_y))
        

bfs()
if visited[n-1][m-1]==1:
    print(1)
else:
    print(0)
