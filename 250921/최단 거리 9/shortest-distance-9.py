# 250921 (14:28)
import sys 
import heapq 
n, m = map(int, input().split())
path=[-1]*(n+1)
graph=[[]for _ in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

A, B = map(int, input().split())
pq=[(0,A)]
dist=[sys.maxsize]*(n+1)
dist[A]=0
# edges = [tuple(map(int, input().split())) for _ in range(m)]

while pq:
    tmp_dist,tmp_node=heapq.heappop(pq)
    if tmp_dist>dist[tmp_node]: continue 
    for v,w in graph[tmp_node]:
        if dist[v]>dist[tmp_node]+w :
            dist[v]=dist[tmp_node]+w 
            path[v]=tmp_node 
            heapq.heappush(pq,(dist[v],v))

print(dist[B])

# for i in range(A,B+1):
#     print(path[i],end=" ")

route=[]
cur=B 
# 여기가 중요.
while cur!=-1:
    route.append(cur)
    cur=path[cur] #그다음 path 
route.reverse()
print(*route)



