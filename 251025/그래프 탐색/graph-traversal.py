
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

visited=[0]*(n+1)
graph=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(len(edges)):
    a,b=edges[i]
    graph[a][b]=1
    graph[b][a]=1 

def dfs(vertex):
    visited[vertex]=1 
    for i in range(n+1):
        if not visited[i] and graph[vertex][i]:
            # visited[i]=1 
            dfs(i)

dfs(1)
print(sum(visited)-1)