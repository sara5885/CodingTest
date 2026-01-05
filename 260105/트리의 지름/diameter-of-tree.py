import sys
sys.setrecursionlimit(100010)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for a,b,w in edges:
    graph[a].append((b,w))
    graph[b].append((a,w))

max_node, max_dist=0,0

def dfs(node, dist):
    global max_node, max_dist 
    global visited 
    if max_dist<dist :
        max_dist=dist 
        max_node=node 
    for n_node, n_dist in graph[node]:
        if visited[n_node]==0:
            visited[n_node]=1 
            dfs(n_node, dist+n_dist)
    return max_dist,max_node

s_dist, s_node = dfs(1,0)
ans,_=dfs(s_node,0)

print(ans)