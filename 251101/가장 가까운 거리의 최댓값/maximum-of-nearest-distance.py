#251101 (15:27)
import heapq 
import sys 
INT_MAX=sys.maxsize 
n, m = map(int, input().split())
a, b, c = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph=[[] for _ in range(n+1)]

for x,y,w in edges:
    graph[x].append((y,w))
    graph[y].append((x,w))

ans=-1
for i in range(1,n+1):
    if i==a or i==b or i==c:
        continue 
    dist_i=[INT_MAX]*(n+1)
    dist_i[i]=0
    pq=[]
    heapq.heappush(pq,(0,i))
    while pq:
        dist, node = heapq.heappop(pq)
        if dist_i[node]!=dist : continue 

        for v,w in graph[node]:
            tmp_dist=dist_i[node]+w 
            if tmp_dist<dist_i[v]:
                dist_i[v]=tmp_dist 
                heapq.heappush(pq,(tmp_dist,v))
    min_in_i=INT_MAX 

    for j in (a,b,c):
        min_in_i=min(min_in_i,dist_i[j])
    # print(i, dist_i)
    # print(min_in_i)
    if min_in_i>ans:
        ans=min_in_i

print(ans)
