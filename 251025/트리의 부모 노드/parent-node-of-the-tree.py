# 251025 (14:21)
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
parent_arr=[0]*(n+1)
# grid=[[0]*(n+1) for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)
    # grid[i][j]=1 
    # grid[j][i]=1 

def dfs(node):
    visited[node]=1
    for i in range(n+1):
        if not visited[i] and i in graph[node]:
            parent_arr[i]=node 
            visited[i]=1 
            dfs(i)

dfs(1)
for i in range(2,n+1):
    print(parent_arr[i])