# 260115 (12:03)
from collections import deque 
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

graph=[[] for _ in range(n+1)]
lived=deque()
parent=[0]*(n+1)

for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)

for i in range(2,n+1):
    if len(graph[i])==1:
        # print(i, graph[i])
        lived.append(i)

def set_parent(node):
    global parent
    parent[node]=-1 #자기자신 
    pq=deque([node])

    while pq:
        n=pq.popleft()
        for child in graph[n]:
            if not parent[child]:
                parent[child]=n
                pq.append(child)
set_parent(1)


turn = 'A'
while lived:
    node=lived.pop()
    if parent[node]!=1:
        lived.append(parent[node])

    if turn=='A':
        turn='B'
    else: 
        turn='A'

if turn=='B':
    print(1)
else:
    print(0)




