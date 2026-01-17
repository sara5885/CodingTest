# 260117 (14:02)
import sys 
INT_MAX=sys.maxsize 
from collections import deque
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

graph=[[] for _ in range(10001)]
for i,j, w in edges:
    graph[i].append((j,w))
    graph[j].append((i,w))

ans=0

def compute_dist(i,j):
    visited=[0]*(10001)
    dist=[0]*(10001)
    visited[i]=1
    pq=deque([i])
    while pq:
        node=pq.popleft()
        if node==j: return dist[node]
        for child,weight in graph[node]:
            if not visited[child]:
                visited[child]=1
                pq.append(child)
                dist[child]=dist[node]+weight

    return -1 
        

for i in range(1,n):
    for j in range(i+1,n+1):
        dist=compute_dist(i,j)
        if dist!=-1:
            ans=max(ans,dist)

print(ans)