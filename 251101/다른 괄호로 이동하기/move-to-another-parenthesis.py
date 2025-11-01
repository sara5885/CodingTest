# 251101 (15:48)
import heapq 
import sys 
INT_MAX=sys.maxsize 
n, a, b = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

ans=-1
def dijkstra(x,y): #i,j가 start node이고 모든 node에 대해 거리 
    dist=[[INT_MAX for _ in range(n+1)] for _ in range(n+1)]
    dist[x][y]=0
    pq=[]
    heapq.heappush(pq,(0,(x,y)))
    while pq:
        w, (cx,cy)= heapq.heappop(pq)
        if dist[cx][cy]!=w : continue 
        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny=cx+dx, cy+dy 
            if 1<=nx<=n and 1<=ny<=n :
                if grid[cx-1][cy-1]==grid[nx-1][ny-1]:
                    tmp_dist=a+dist[cx][cy]
                else:
                    tmp_dist=b+dist[cx][cy]
                if tmp_dist<dist[nx][ny]:
                    dist[nx][ny]=tmp_dist 
                    heapq.heappush(pq,(tmp_dist,(nx,ny)))
    max_dist=-1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i,j)==(x,y): continue 
            if dist[i][j]==INT_MAX:continue 
            max_dist=max(max_dist,dist[i][j])
    
    return max_dist 



for i in range(1,n+1):
    for j in range(1,n+1):
        tmp_dist=dijkstra(i,j)
        ans=max(ans,tmp_dist)

print(ans)