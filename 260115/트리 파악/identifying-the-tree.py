import sys
sys.setrecursionlimit(100000)
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
# root - 모든 leaf node까지의 거리의 합 
dist=[0]*(n+1) #루트에서 i까지의 dist 
ans=0 
for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)

def dfs(node):
    global ans 
    visited[node]=1
    is_leaf=True 
    for i in graph[node]:
        if visited[i] : continue 
        is_leaf=False 
        visited[i]=1 
        dist[i]=dist[node]+1 
        dfs(i)
    if is_leaf:
        ans+=dist[node]

dfs(1)
if ans%2==1:
    print(1)
else:
    print(0)