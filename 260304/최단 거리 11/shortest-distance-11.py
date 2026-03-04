# 260304 (13:11)
import sys 
import heapq 
INT_MAX=sys.maxsize 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

dist=[INT_MAX]*(n+1)
dist[B]=0
path=[-1]*(n+1)
# 뒤집어서 경로 구해야하는데 양방향이라 출발, 시작만 다르게 함 
graph=[[0 for _ in range(n+1)] for _ in range(n+1)]

# for i,j,w in edges:
#     graph[i].append([j,w])
#     graph[j].append([i,w])

for i,j, w in edges:
    graph[i][j]=w
    graph[j][i]=w 

pq=[]
heapq.heappush(pq,(B,0))
while pq:
    c_node, c_weight = heapq.heappop(pq)
    if c_weight > dist[c_node]: continue 
    for n_node in range(1,n+1):
        if graph[c_node][n_node]==0 : continue 
        if dist[n_node]>dist[c_node]+graph[c_node][n_node]:
            dist[n_node]=dist[c_node]+graph[c_node][n_node]
            heapq.heappush(pq,(n_node, dist[n_node]))
            path[n_node]=c_node 
print(dist[A])
tmp=A
print(tmp,end=" ")
while tmp!=B:
    for i in range(1,n+1):
        if graph[tmp][i]==0: continue 
        
        if dist[tmp]==dist[i]+graph[tmp][i]:
            tmp=i
            print(tmp,end=" ")
            break 
