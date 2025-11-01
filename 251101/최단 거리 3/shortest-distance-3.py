import heapq 
import sys 
INT_MAX=sys.maxsize 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.
graph=[[] for _ in range(n+1)]
for x,y,w in edges:
    graph[x].append((y,w))
    graph[y].append((x,w))

dist_a=[INT_MAX]*(n+1)
dist_a[A]=0
pq=[(0,A)]
while pq:
    dist,node = heapq.heappop(pq)
    if dist_a[node]!=dist:
        continue #dummy node 
    for v,w in graph[node]:
        tmp_dist=w+dist 
        if tmp_dist<dist_a[v]:
            dist_a[v]=tmp_dist 
            heapq.heappush(pq,(tmp_dist,v))

print(dist_a[B])