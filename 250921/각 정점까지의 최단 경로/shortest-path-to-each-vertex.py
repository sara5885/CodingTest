# 250921 (13:59)
import sys 
import heapq 
n, m = map(int, input().split())
k = int(input())
# edges = [tuple(map(int, input().split())) for _ in range(m)]

source=k 
dist=[sys.maxsize]*(n+1)
dist[k]=0 

pq=[(0,k)] #start point 

# 많은 edge를 대비해서 adjacent list 사용하기
graph=[[]for _ in range(n+1)]
for _ in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))



while pq:
    tmp_dist,tmp_node=heapq.heappop(pq)
    if dist[tmp_node]!=tmp_dist : continue 
    for v,w in graph[tmp_node]: # 해당 node의 인접 노드만 확인하기 
        if dist[v]>dist[tmp_node]+w:
            dist[v]=dist[tmp_node]+w 
            heapq.heappush(pq,(dist[v],v))

for i in range(1,n+1):
    if dist[i]==sys.maxsize:
        print(-1)
    else:
        print(dist[i])
