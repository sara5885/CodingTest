#260118 (14:01)
import sys 
INT_MAX=sys.maxsize 
from collections import deque 
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# for1 모든 노드에 대해 진행 
# for1-1 각 노드에 대해 최대 거리 구하기 

graph=[[] for _ in range(n+1)]

for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

def bfs(node):
    pq=deque([node])
    visited=[0]*(n+1)
    visited[node]=1 
    m_dist, m_node=0,0
    dist=[0]*(n+1)
    while pq:
        c_node=pq.popleft()
        for child in graph[c_node]:
            if not visited[child]:
                visited[child]=1
                pq.append(child)
                dist[child]=dist[c_node]+1
                if dist[child]>m_dist:
                    m_dist=dist[child]
                    m_node=child 
    return m_node, m_dist 

num,_= bfs(1)
_,dist=bfs(num)
print((dist+1)//2)