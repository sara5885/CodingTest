import sys 
import heapq
INT_MAX=sys.maxsize 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

if A==B : print(0)
else:
    dist=[INT_MAX]*(n+1)
    pq=[]
    heapq.heappush(pq,(A,0))
    graph=[[] for _ in range(n+1)]

    for i,j,w in edges:
        graph[i].append([j,w])
        graph[j].append([i,w])

    while pq:
        c_node, c_dist = heapq.heappop(pq)
        for n_node, n_weight in graph[c_node]:
            cand=c_dist+n_weight 
            if cand < dist[n_node]:
                dist[n_node]=cand
                heapq.heappush(pq,(n_node,cand))

    print(dist[B])