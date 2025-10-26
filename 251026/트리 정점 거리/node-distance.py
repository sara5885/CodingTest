# 251026 (13:25)
n, m = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
queries = [tuple(map(int, input().split())) for _ in range(m)]
graph=[[] for _ in range(n+1)]
for a,b,w in edges:
    graph[a].append((b,w))
    graph[b].append((a,w))

def dfs(c_node,dist, l_node):
    # print(f"c_node:{c_node}, dist:{dist}, l_node:{l_node}")
    visited[c_node]=1 
    if c_node==l_node:
        return dist 
    for i,w in graph[c_node]:
        if not visited[i]:
            visited[i]=1
            ans=dfs(i,dist+w,l_node)
            if ans!=0:
                return ans 
    return 0

for s,e in queries:
    visited=[0]*(n+1)
    ans=dfs(s,0,e)
    print(ans)
