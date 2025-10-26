#251016 (14:00)
# total_depth_sum 누적 합 : dfs 안에서 leaf node인 경우 더하기 
import sys 
sys.setrecursionlimit(1000000)
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
ans=0
for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

def dfs(node,depth):
    global ans
    visited[node]=1
    cnt=1 
    leaf_flag=True 
    for i in graph[node]:
        if not visited[i]:
            visited[i]=1 
            leaf_flag=False 
            dfs(i,depth+1)
    if leaf_flag:#leaf인경우에만 depth더하기 
        ans+=depth 


# 루트-leaf노드까지 총 거리 
dfs(1,0)
# print(cnt)
if (ans)%2==0:
    print(0)
else:
    print(1)