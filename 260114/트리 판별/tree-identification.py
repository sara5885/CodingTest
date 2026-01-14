MAX_NUM=10000
m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]
in_deg=[[] for _ in range(m+1)]
graph=[[] for _ in range(MAX_NUM+1)]
root=-1 
used=[0]*(MAX_NUM+1) #실제 사용되는 노드 번호 
visited=[0]*(MAX_NUM+1) #dfs할 때 사용 
deg=[0]*(MAX_NUM+1) #각 node별 들어오는 edge 개수 
is_tree=True 
# 1. root node가 딱 한 개 (in_deg=[[] for _ in range(m)]), in_deg: empty 
# 2. root 제외 parent는 딱 한개 (in_deg) len(in_deg[i])==1 
# 3. root를 시작으로 모든 node에 도달 (dfs, visited)

# root node에서 모든 정점으로 갈 수 있는지 판단하는 법
# : root node를 시작으로 dfs 한 번 돌면 됨 : visited[root]=True, dfs(root)
# dfs에서 방문한 node들 표시하고 
for i,j in edges:
    graph[i].append(j)
    used[i]=1
    used[j]=1
    deg[j]+=1

def dfs(node):
    for i in graph[node]:
        if visited[i]: continue 
        visited[i]=1
        dfs(i)

# 루프노드 찾기
for i in range(1,MAX_NUM+1):
    if used[i] and deg[i]==0:
        if root!=-1:
            is_tree=False 
        root=i

if root==-1:
    is_tree=False 

for i in range(1,MAX_NUM+1):
    if i!=root and used[i] and deg[i]!=1:
        is_tree=False 

if is_tree and root!=-1:
    visited[root]=True 
    dfs(root)

for i in range(1,MAX_NUM+1):
    if used[i] and not visited[i]:
        is_tree=False 
        break
if is_tree:
    print(1)
else:
    print(0)