#260118 (14:01)
import sys 
INT_MAX=sys.maxsize 
from collections import deque 
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# for1 모든 노드에 대해 진행 
# for1-1 각 노드에 대해 최대 거리 구하기 

graph=[[] for _ in range(n+1)]

for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

ans =INT_MAX
for i in range(1,n+1):
    pq=deque([i])
    visited=[0]*(n+1)
    dist=[0]*(n+1)
    c_max_dist=0
    while pq:
        node=pq.popleft()
        for child in graph[node]:
            if not visited[child]:
                visited[child]=1
                pq.append(child)
                dist[child]=dist[node]+1
                c_max_dist=max(c_max_dist, dist[child])
    ans=min(ans,c_max_dist)


print(ans)