# 260114 (12:08)

n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

graph=[[] for _ in range(n)]
root=-1 
ans=0

for i in range(n):
    p=parent[i]
    if p==-1:
        root=i
        continue 
    graph[p].append(i)

# for i in graph:
#     print(i)

# root부터 순회해서 leaf노드 
def dfs(node):
    global ans 
    
    if node==remove_node:
        return 
    is_leaf=True 
    for i in graph[node]: # 자식들 순회 
        if i==remove_node: #지워진 자식이면 pass 
            continue 
        dfs(i) #지워진 자식이 아닌 살아있는 자식이면 dfs 들어감 
        is_leaf=False #dfs를 했다는 건 살아있는 자식이 있다는 것 => 해당 node는 leaf가 아님 
    
    if is_leaf:
        ans+=1 
    # leaf면 자연스럽게 is_leaf=True 

dfs(root)
print(ans)