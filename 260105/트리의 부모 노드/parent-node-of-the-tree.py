# 260105 (15:19)
import sys
sys.setrecursionlimit(100000)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

parent_arr=[-1]*(n+1)
parent_arr[1]=1 
visited=[0]*(n+1)

graph=[[] for _ in range(n+1)]

# 아직 누가 parent고 누가 child인지는 모름 
for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)

def dfs(node):
    visited[node]=1
    for i in graph[node]: # i : 연결된 node 번호 
        if visited[i]==0:
            visited[i]=1
            parent_arr[i]=node 
            dfs(i)

dfs(1)
for i in range(2,n+1):
    print(parent_arr[i])