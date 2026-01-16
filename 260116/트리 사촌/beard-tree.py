#260116 (12:00)
from collections import deque 
n, k = map(int, input().split())
sequence = list(map(int, input().split()))
graph=[[] for _ in range(1000001)]
depth={}
parent={}
leaf=deque([sequence[0]])
root=sequence[0]

node=root 
for i in range(1,n):
    # +1 차이 
    if sequence[i] -1 == sequence[i-1]:
        graph[node].append(sequence[i])
    # 더 많은 차이 
    else:
        node=leaf.popleft()
        graph[node].append(sequence[i])
    parent[sequence[i]]=node
    leaf.append(sequence[i])


# depth 설정하기 
depth[root]=0 
def bfs():
    pq=deque()
    pq.append(root)
    visited=set()
    visited.add(root)

    while pq:
        n=pq.popleft()
        for i in graph[n]:
            if i not in visited :
                depth[i]=depth[n]+1 
                visited.add(i)
                pq.append(i)
        
bfs()
# for node,i in depth.items():
#     print(node, i)

# print(depth)
# print(parent)
ans=0
# t_depth=depth[k]
for key,value in depth.items():
    if value==depth[k] and parent[key]!=parent[k]:
        ans+=1

print(ans)
