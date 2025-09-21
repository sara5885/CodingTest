# 250921 (13:59)
import sys 
import heapq 
n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

source=k 
dist=[sys.maxsize]*(n+1)
dist[k]=0 

pq=[(0,k)] #start point 

while pq:
    tmp_dist,tmp_node=heapq.heappop(pq)
    if dist[tmp_node]!=tmp_dist : continue 
    for i in range(m):
        s_n,d_n,value=edges[i]
        if tmp_node!=s_n and tmp_node!=d_n:
            continue 
        elif tmp_node==d_n:
            s_n,d_n=d_n,s_n
        if dist[d_n]>dist[s_n]+value:
            dist[d_n]=dist[s_n]+value 
            heapq.heappush(pq,(dist[d_n],d_n))

for i in range(1,n+1):
    if dist[i]==sys.maxsize:
        print(-1)
    else:
        print(dist[i])
