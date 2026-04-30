n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

neighbor=[[] for _ in range(n+1)]

# dfs 
visited=[0]*(n+1)
order =[]
def dfs(node):
    visited[node]=1
    for neigh in neighbor[node]:
        if not visited[neigh]:
            dfs(neigh)
    order.append(node)

for a,b in edges:
    neighbor[a].append(b)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)

for i in order[::-1]:
    print(i,end=" ")

    
