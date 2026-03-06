# 260306 (15:20)
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph=[[] for _ in range(n+1)]
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

# 1번 정점에서 갈 수 있는 정점 수 
visited=[0]*(n+1)
visited[1]=1 

def dfs(idx):
    visited[idx]=1 
    for neigh in graph[idx]:
        # print(neigh)
        if visited[neigh]: continue 
        visited[neigh]=1 
        dfs(neigh)
dfs(1)
print(sum(visited)-1)