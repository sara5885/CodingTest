# 2601187 (13:40)
import sys 
INT_MAX=sys.maxsize 
from collections import deque 
n, d = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
from_v, to_v, length = zip(*edges)
from_v = list(from_v)
to_v = list(to_v)
length = list(length)

graph=[[] for _ in range(n+1)]
for i,j,w in edges:
    graph[i].append((j,w))
    graph[j].append((i,w))
# for i in graph:
#     print(i)
# 트리의 지름 
# 만약 지름이 여러개라면 dist가 가장 짧은것 
def bfs(node):
    visited=[0]*(n+1)
    visited[node]=1
    dist=[0]*(n+1)
    depth=[0]*(n+1)
    max_num, max_depth=0,0
    pq=deque([node])
    while pq:
        c_node=pq.popleft()
        for child,c_dist in graph[c_node]:
            if not visited[child]:
                visited[child]=1
                dist[child]=dist[c_node]+c_dist 
                depth[child]=depth[c_node]+1
                if depth[child]>max_depth :
                    max_num=child 
                    max_depth=depth[child]
                pq.append(child)
    return max_num, max_depth 

def bfs2(node):
    visited=[0]*(n+1)
    visited[node]=1
    dist=[0]*(n+1)
    depth=[0]*(n+1)
    min_dist, max_num, max_depth=INT_MAX,0,0
    pq=deque([node])
    while pq:
        c_node=pq.popleft()
        for child,c_dist in graph[c_node]:
            if not visited[child]:
                visited[child]=1
                dist[child]=dist[c_node]+c_dist 
                depth[child]=depth[c_node]+1
                # if c_node==4: print(child, c_dist)
                if depth[child]>max_depth or (depth[child]==max_depth and dist[child]<min_dist): 
                    min_dist=dist[child]
                    max_num=child 
                    max_depth=depth[child]
                pq.append(child)
    return max_num, min_dist 

tmp,_=bfs2(1)
_,ans=bfs2(tmp)
# print("tmp:",tmp)
# print(ans)
if ans%d==0:
    print(ans//d)
else:
    print(ans//d+1)