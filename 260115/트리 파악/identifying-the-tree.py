import sys
sys.setrecursionlimit(100000)
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
visited=[0]*(n+1)
depth=[0]*(n+1)
graph=[[] for _ in range(n+1)]
ans=0

for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)

def dfs(x):
    global ans 
    is_leaf=True 
    for y in graph[x]:
        if visited[y]: continue 
        visited[y]=1
        is_leaf=False
        depth[y]=depth[x]+1
        dfs(y) 
    if is_leaf: ans+=depth[x]

visited[1]=1
dfs(1)

if ans%2==1:
    print(1)
else:
    print(0)

