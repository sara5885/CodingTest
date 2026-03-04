#260304 (12:38)
import sys 
import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())
INT_MAX=sys.maxsize 

dist=[INT_MAX]*(n+1)
dist[A]=0
path=[-1]*(n+1) #A->B까지의 최단경로 

graph=[[] for _ in range(n+1)]

for i,j,w in edges:
    graph[i].append([j,w])
    graph[j].append([i,w])

pq=[]
heapq.heappush(pq,(A,0))
while pq:
    c_node, c_weight=heapq.heappop(pq)
    for n_node, n_weight in graph[c_node]:
        if n_weight > dist[n_node]: continue 
        tmp_dist=n_weight+c_weight 
        if dist[n_node]>tmp_dist:
            dist[n_node]=tmp_dist
            heapq.heappush(pq,(n_node,tmp_dist))
            path[n_node]=c_node 

print(dist[B])

# 도착점을 시작으로 거꾸로 이동 
tmp=B
arr=[]
while tmp!=A:
    arr.append(tmp)
    tmp=path[tmp]
arr.append(A)
arr.reverse()

for i in arr:
    print(i,end=" ")