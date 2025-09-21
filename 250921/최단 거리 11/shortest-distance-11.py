# 250921 (19:57)
import sys 
import heapq 
n, m = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]
graph=[[]for _ in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

for i in range(1,n+1):
    graph[i].sort()
A, B = map(int, input().split())
pq=[(0,B)]
dist=[sys.maxsize]*(n+1)
dist[B]=0
path=[-1]*(n+1)


while pq:
    tmp_dist,tmp_node=heapq.heappop(pq)
    if tmp_dist>dist[tmp_node]:
        continue 
    for v,w in graph[tmp_node]:
        if dist[v]>dist[tmp_node]+w:
            dist[v]=dist[tmp_node]+w 
            heapq.heappush(pq,(dist[v],v))
            path[v]=tmp_node 

print(dist[A])
x=A
while x!=B:
    for neighbor,weight in graph[x]: # already sorted 
        # if dist[neighbor]==dist[x]+weight:
        if dist[x]==dist[neighbor]+weight:
            print(x,end=" ")
            x=neighbor 
            break #해당 node에 대해 가장 작은 node 구한 것 
print(B)


