# 240921 (13:24) (13:45)
import sys 
import heapq 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
dist=[sys.maxsize]*(n+1) #다 최댓값으로 되어있음 
dist[1]=0 # source 
pq=[(0,1)] #dist, node number 


while pq: 
    tmp_dist,tmp_node=heapq.heappop(pq)
    if tmp_dist>dist[tmp_node] : continue #dist array랑 
    for i in range(len(edges)):
        s_n, d_n,v=edges[i]
        if s_n==tmp_node:
            if tmp_dist+v < dist[d_n]:
                dist[d_n]=tmp_dist+v 
                heapq.heappush(pq,(tmp_dist+v, d_n))

# print(dist)
    
for i in range(2,n+1):
    if dist[i]==sys.maxsize:
        print(-1)
    else:
        print(dist[i])