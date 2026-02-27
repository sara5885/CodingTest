import sys 
import heapq
INT_MAX=sys.maxsize 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph=[[] for _ in range(n+1)]

for i,j,w in edges:
    graph[i].append((j,w))

dist=[INT_MAX]*(n+1)
pq=[]
heapq.heappush(pq,(1,0))

while pq:
    num, c_dist = heapq.heappop(pq)
    for node,weight in graph[num]:
        cand=c_dist+weight
        if cand < dist[node]: 
            dist[node]=cand
            heapq.heappush(pq,(node,cand))

for i in range(2,n+1):
    if dist[i]==INT_MAX:
        print(-1)
    else:        
        print(dist[i])