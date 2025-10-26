# 251026 (12:33)
m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph=[[] for _ in range(10001)]
#누군가의 자식으로 이미 선정된 node 
child=set()
tree_flag=True 
node=set()
root_cand=[]
for a,b in edges:
    if a not in child and a not in root_cand:
        root_cand.append(a)
    if b in child:
        tree_flag=False 
        break
    if b in root_cand:
        root_cand.remove(b)
    graph[a].append(b)
    child.add(b)
    node.add(a)
    node.add(b)
# 2개이상의 그래프. 어떤 그래프가 cycle일 때. 
# dfs로 모든 그래프 도달 가능한지 확인 
visited=[0]*10001
def dfs(node):
    cnt=1 
    visited[node]=1
    for i in graph[node]:
        if not visited[i]:
            visited[i]=1
            cnt+=dfs(i)
    return cnt 


# print(root_cand)
if len(root_cand)!=1:
    tree_flag=False
else:
    ans=dfs(root_cand[0])
    if ans!=len(node):
        tree_flag=False

if tree_flag:
    print(1)
else:
    print(0)