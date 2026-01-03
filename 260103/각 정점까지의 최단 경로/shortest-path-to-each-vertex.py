import heapq 
import sys 

INT_MAX=sys.maxsize 


n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph=[[] for _ in range(n+1)]
dist=[INT_MAX]*(n+1)

for i in range(m):
    x,y,z=edges[i]
    graph[x].append((y,z))
    graph[y].append((x,z))

pq=[]
heapq.heappush(pq,(0,k))
dist[k]=0

while pq:
    length, node_num=heapq.heappop(pq)

    # if dist[node_num]<length:
    #     continue 
    if dist[node_num]<length:
    #같은 정점 원소 여러번 들어갈 수 있는데 min_dist가 최신 dist[min_index]랑 다르면 패스 
        continue 
    for n_node, n_dist in graph[node_num]:
        cost=dist[node_num]+n_dist 
        if dist[n_node]>cost :
            dist[n_node]=cost
            heapq.heappush(pq,(cost,n_node))

for i in range(1,n+1):
    if dist[i]==INT_MAX:
        print(-1)
    else:
        print(dist[i])