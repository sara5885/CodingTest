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

all_dists={}
ans=-1
for i in (a,b,c):
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
    all_dists[i]=dist_i
ans=-1 
for i in range(1,n+1):
    if i in (a,b,c): continue 
    dist_to_a = all_dists[a][i]
    dist_to_b = all_dists[b][i]
    dist_to_c = all_dists[c][i]

    min_dist_to_abc = min(dist_to_a, dist_to_b, dist_to_c)
    
    # (예외 처리: a,b,c와 연결되지 않은 노드는 무시)
    if min_dist_to_abc == INT_MAX:
        continue

    # "가장 짧은 거리"가 최대가 되는 노드를 찾음
    if min_dist_to_abc > ans:
        ans = min_dist_to_abc
print(ans)
