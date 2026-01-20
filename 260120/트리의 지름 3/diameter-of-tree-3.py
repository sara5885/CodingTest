# 260120 (13:52)
from collections import deque 
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

max_list=[]
graph=[[] for _ in range(n+1)]
for i,j,w in edges:
    graph[i].append((j,w))
    graph[j].append((i,w))

def bfs(node):
    pq=deque([node])
    visited=[0]*(n+1)
    visited[node]=1 
    dist=[0]*(n+1)
    max_num, max_dist =0,0
    while pq:
        c_node=pq.popleft()
        for child,w in graph[c_node]:
            if not visited[child]:
                visited[child]=1
                dist[child]=dist[c_node]+w
                pq.append(child)
                if dist[child]>max_dist:
                    max_dist=dist[child]
                    max_num=child 

    return max_num, max_dist, dist

t_num, _,_=bfs(1)
t2_num,_,dist_arr1=bfs(t_num)
_,_,dist_arr2=bfs(t2_num)
dist_arr=dist_arr1.copy()
for i in range(1,n+1):
    if i!=t_num:
        dist_arr.append(dist_arr2[i])

dist_arr.sort(reverse=True)
print(dist_arr[1])
# print(dist_arr)
