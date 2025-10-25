n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for i,j,w in edges:
    graph[i].append((j,w))
    graph[j].append((i,w))
s=1 
e=1
max_dist=0
max_node=0 
def dfs(node,dist):
    global visited
    global max_dist,max_node 
    visited[node]=1 
    if max_dist<dist:
        max_dist=dist 
        max_node=node 
    for i,weight in graph[node]:
        if not visited[i]:
            visited[i]=1
            dfs(i,dist+weight)
    return max_node,max_dist
    

e,_=dfs(1,0)
visited=[0]*(n+1)
max_dist=0
max_node=0 
s,ans=dfs(e,0)
# print(s,e)
print(ans)