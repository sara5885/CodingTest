#250914 (17:37)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

visited=[0]*(n+1)
grid=[
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]
for i in range(len(edges)):
    a,b=edges[i]
    grid[a][b]=1
    grid[b][a]=1 

def dfs(vertex):
    visited[vertex]=1
    for i in range(n+1): 
        # linked vertex : 
        if visited[i]==0 and grid[vertex][i]==1:
            visited[i]=1
            dfs(i)


dfs(1)
print(sum(visited)-1)