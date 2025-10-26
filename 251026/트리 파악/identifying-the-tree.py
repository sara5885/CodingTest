#251016 (14:00)
# 꼭 visited가 있어야 하는가. 
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for a,b in edges:
    graph[a].append(b)

def dfs(node):
    visited[node]=1
    cnt=1 
    for i in graph[node]:
        if not visited[i]:
            visited[i]=1 
            cnt+=dfs(i)
    return cnt 



# 루트-leaf노드까지 총 거리 
cnt=dfs(1)
# print(cnt)
if (cnt-1)%2==0:
    print(0)
else:
    print(1)