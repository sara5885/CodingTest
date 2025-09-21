#250921 (20:46) ()
import sys 
import heapq 
n, m = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]
graph=[[]for _ in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

A, B = map(int, input().split())
dist=[sys.maxsize]*(n+1) 
dist[A]=0
pq=[(0,A)] #tuple에 대한 list. tuple에 대한 tuple 아님 ((0,A))

while pq:
    tmp_dist,tmp_node=heapq.heappop(pq)
    if tmp_dist!=dist[tmp_node]:continue 
    for v,w in graph[tmp_node]:
        if dist[v]>dist[tmp_node]+w:
            dist[v]=dist[tmp_node]+w 
            heapq.heappush(pq, (dist[v],v))

print(dist[B])
