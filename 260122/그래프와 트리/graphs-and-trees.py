# 260122 (18:09)
from collections import deque 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

tree_cnt=0

# 트리이 아니고 bfs 하면 되는건가?
graph=[[] for _ in range(n+1)]
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

visited=[0]*(n+1)
def bfs(node):
    global visited 
    global tree_cnt 

    pq=deque([node])
    cycle_flag=False 
    while pq:
        c_node=pq.popleft()
        for child in graph[c_node]:
            if visited[child]: 
                # print("cycle:", c_node, child)
                cycle_flag=True 
                return
            else:
                visited[child]=1
                pq.append(child)
                if c_node in graph[child]: 
                    graph[child].remove(c_node)
    if not cycle_flag:
        tree_cnt+=1


for i in range(1,n+1):
    if not visited[i]:
        visited[i]=1
        bfs(i)
    

print(tree_cnt)