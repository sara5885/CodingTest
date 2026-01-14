n, m = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
queries = [tuple(map(int, input().split())) for _ in range(m)]

graph=[[] for _ in range(n+1)]
for i,j,l in edges:
    graph[i].append((j,l))
    graph[j].append((i,l))

# i부터 j까지 거리 
def dfs(i,j,len): 
    
    if i==j:
        return len 
    for child,c_len in graph[i]:
        if not visited[child]:
            visited[child]=1
            result=dfs(child,j,len+c_len)
            if result is not None:
                return result
    




for i,j in queries:
    if i==j:
        print(0)
        continue 
    visited=[0]*(n+1)
    visited[i]=1 
    print(dfs(i,j,0))

    