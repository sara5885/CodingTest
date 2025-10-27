# 251027 (19:33)
import sys 
INT_MAX=sys.maxsize
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

visited=[0]*(n+1)
dist=[INT_MAX]*(n+1)
graph=[[0]*(n+1) for _ in range(n+1)]

for x,y,w in edges:
    if graph[x][y]==0 or graph[x][y]>w:
        graph[x][y]=w
        graph[y][x]=w 

dist[1]=0
ans=0
for i in range(1,n+1): #n개의 node에 대해 진행 
    # min_index : dist가 가장 작은 i 찾기 
    min_idx=-1 
    for j in range(1,n+1):
        if visited[j]:
            continue
        if min_idx==-1 or dist[min_idx]>dist[j]:
            min_idx=j 
    visited[min_idx]=1
    ans+=dist[min_idx]
    for j in range(1,n+1):
        if graph[min_idx][j]==0:
            continue 
        dist[j]=min(dist[j], graph[min_idx][j]) # 지금까지의 경로가 아닌 기준 노드와 현재노드와의 거리 

print(ans)