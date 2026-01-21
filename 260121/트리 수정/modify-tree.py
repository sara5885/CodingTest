from collections import deque 
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
from_v, to_v, weight = zip(*edges)
from_v = list(from_v)
to_v = list(to_v)
weight = list(weight)

# Please write your code here.
# 1. 모든 edge에 대해 각각 끊어보기
# 2. 끊긴 두 트리 각각의 지름 구하기 
# 3. 그리고 이렇게 끊긴 각각의 지름에 원래의 edge weight 더해보기 
graph=[[] for _ in range(n+1)]
for i,j,w in edges:
    graph[i].append((j,w))
    graph[j].append((i,w))

def compute_dist(start, avoid):
    pq=deque([start])
    visited=[0]*(n+1)
    visited[start]=1
    dist=[0]*(n+1)
    max_num,max_dist=start,0
    while pq:
        c_node=pq.popleft()
        for child,weight in graph[c_node]:
            # print(visited[child])
            if child==avoid or visited[child]:
                continue 
            visited[child]=1
            dist[child]=dist[c_node]+weight
            pq.append(child)
            if dist[child]>max_dist:
                max_dist=dist[child]
                max_num=child 
    t_num=max_num
    pq=deque([t_num])
    visited=[0]*(n+1)
    visited[t_num]=1
    dist=[0]*(n+1)
    f_max_dist=0
    while pq:
        c_node=pq.popleft()
        for child,weight in graph[c_node]:
            if child==avoid or  visited[child]==1:
                continue
            visited[child]=1
            dist[child]=dist[c_node]+weight
            pq.append(child)
            if dist[child]>f_max_dist:
                f_max_dist=dist[child]
                
    return f_max_dist


ans=0
for i,j,w in edges:
    d1=compute_dist(i, j)
    d2=compute_dist(j,i)
    ans=max(ans, d1+d2+w)
    # print(i,j,":", ans)
    # print(d1,d2)
print(ans)

