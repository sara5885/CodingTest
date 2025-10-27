# 251027 (20:04)
import heapq
import sys 
INT_MAX=sys.maxsize 

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# adjacency list 
graph=[[] for _ in range(n+1)]
pq=[]

dist=[INT_MAX]*(n+1)
visited=[0]*(n+1)

for x,y,w in edges:
    graph[x].append((y,w))
    graph[y].append((x,w))

dist[1]=0


heapq.heappush(pq,(0,1))

ans=0

while pq:
    min_dist,min_node=heapq.heappop(pq)

    if visited[min_node]:
        continue 
    visited[min_node]=1
    ans+=min_dist 

    for t_index, t_dist in graph[min_node]:
        if dist[t_index]>t_dist:
            dist[t_index]=t_dist
            heapq.heappush(pq,(t_dist,t_index))

print(ans)