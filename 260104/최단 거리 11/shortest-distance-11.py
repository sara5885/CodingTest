import sys 
import heapq 
INT_MAX=sys.maxsize 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.
graph=[[0 for _ in range(n+1)] for _ in range(n+1)]

for edge in edges:
    a,b,c=edge 
    graph[a][b]=c
    graph[b][a]=c 

dist=[INT_MAX]*(n+1) # B에서 다른 노드들까지의 거리 
pq=[]
heapq.heappush(pq,(B,0))
dist[B]=0 

while pq:
    c_node, c_dist = heapq.heappop(pq)
    if dist[c_node]<c_dist:
        continue 
    for i in range(1,n+1):
        if graph[c_node][i]==0: continue 
        if dist[i]>dist[c_node]+graph[c_node][i]:
            dist[i]=dist[c_node]+graph[c_node][i]
            heapq.heappush(pq,(i,dist[i]))

print(dist[A])
x=A
print(x,end=" ")
while x!=B:
    
    for i in range(1,n+1):
        if graph[x][i]==0: continue 
        if dist[x]==dist[i]+graph[x][i]:
            x=i
            break # 현재 node였던 x 그 다음 (숫자가 가장 작은) 노드 발견했으니 for문은 break 
    print(x,end=" ")