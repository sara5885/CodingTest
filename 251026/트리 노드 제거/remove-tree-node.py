#251026 (11:33)
n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())
graph_arr=[1]*n
graph=[[] for _ in range(n)]
root_node=-1
for i in range(n):
    # parent[i] : i-번째 노드의 부모 
    if parent[i]==-1:
        root_node=i
    else:
        graph[parent[i]].append(i)

visited=[0]*n
# remove node
def dfs(node):
    visited[node]=1
    graph_arr[node]=0 
    for child in graph[node]:
        if not visited[child] and graph_arr[child]:
            visited[child]=1 # 중복 
            graph_arr[child]=0 
            dfs(child)
graph[parent[remove_node]]
dfs(remove_node)
# print(graph_arr)
# print(graph)
cnt=0
for i in range(len(graph_arr)):
    # print(f"node:{i}, len(graph[node]):{len(graph[i])}")
    if graph_arr[i] and len(graph[i])==0 : #삭제되지않은 리프노드일 조건 
        cnt+=1
print(cnt)