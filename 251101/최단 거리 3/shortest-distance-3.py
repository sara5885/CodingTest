import heapq 
import sys 
INT_MAX=sys.maxsize 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

graph=[[INT_MAX for _ in range(n+1)] for _ in range(n+1) ]
for x,y,w in edges:
    graph[x][y]=min(graph[x][y],w)
    graph[y][x]=min(graph[y][x],w)
for i in range(1,n+1):
    graph[i][i]=0

dist_a=[INT_MAX]*(n+1)
dist_a[A]=0
pq=[]
heapq.heappush(pq,(0,A))

while pq:
    tmp_dist, tmp_node= heapq.heappop(pq)
    if dist_a[tmp_node]!=tmp_dist:
        continue 
    for v in range(1,n+1):
        v_dist=tmp_dist+graph[tmp_node][v]
        if v_dist<dist_a[v]:
            dist_a[v]=v_dist 
            heapq.heappush(pq,(v_dist,v))
print(dist_a[B])