import sys
from collections import deque 
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

neighbor=[[] for _ in range(n+1)]
# indegree 
pq=deque()
indegree=[0]*(n+1)
for a,b in edges: # adjacent list 생성 & indegree 계산 
    neighbor[a].append(b)
    indegree[b]+=1 

for i in range(1,n+1): # indegree가 0인 노드들 deque에 추가 
    if indegree[i]==0: 
        pq.append(i)

while pq:
    node=pq.popleft()
    print(node,end=" ")
    # 이웃노드들의 indegree -1 
    for neigh in neighbor[node]:
        if indegree[neigh]==0: print("오류 ")
        indegree[neigh]-=1 
        if indegree[neigh]==0: 
            pq.append(neigh)
    


# dfs 
# visited=[0]*(n+1)
# order =[]
# def dfs(node):
#     visited[node]=1
#     for neigh in neighbor[node]:
#         if not visited[neigh]:
#             dfs(neigh)
#     order.append(node)

# for i in range(1,n+1):
#     if not visited[i]:
#         dfs(i)

# for i in order[::-1]:
#     print(i,end=" ")

    
