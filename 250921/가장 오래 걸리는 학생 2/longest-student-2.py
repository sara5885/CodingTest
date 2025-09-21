# 250921 (14:17)
import sys 
import heapq 
n, m = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]

dist=[sys.maxsize]*(n+1)
dist[n]=0
graph=[[]for _ in range(n+1)]
pq=[(0,n)]

for _ in range(m):
    u,v,w=map(int,input().split())
    graph[v].append((u,w)) #반대로 넣어주기 

while pq:
    tmp_dist,tmp_node=heapq.heappop(pq)
    if tmp_dist>dist[tmp_node]:
        continue 
    for v,w in graph[tmp_node]:
        if dist[v]>dist[tmp_node]+w:
            dist[v]=dist[tmp_node]+w 
            heapq.heappush(pq,(dist[v],v))
dist[0]=0
print(max(dist))
