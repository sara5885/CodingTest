# 260304 (16:23)
# import sys
# import heapq 
# INT_MAX=sys.maxsize 

# n, m, x = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]

# graph=[[(INT_MAX, INT_MAX) for _ in range(n+1)] for _ in range(n+1)]
# c_set=set()
# for i,j,l,c in edges:
#     c_set.add(c)
#     if graph[i][j]>(l,c):
#         graph[i][j]=(l,c)
#     if graph[j][i]>(l,c):
#         graph[j][i]=(l,c)

# ans=INT_MAX
# for c_limit in c_set:
#     pq=[]
#     dist=[INT_MAX]*(n+1)
#     heapq.heappush(pq,(0,1))
#     # dijkstra 
#     while pq:
#         c_dist, c_node = heapq.heappop(pq)
#         if dist[c_node] < c_dist : continue 
#         for i in range(2,n+1):
#             if graph[c_node][i]==(INT_MAX,INT_MAX): continue
#             n_weight, n_c= graph[c_node][i]
#             # 조건 : 해당 graph[i][j]의 c가 c_limit 이상이어야함 
#             if n_c < c_limit : continue
#             if dist[i]> n_weight+c_dist:
#                 dist[i]=n_weight+c_dist 
#                 heapq.heappush(pq,(dist[i], i))
#     # A : c_limit
#     # B : dist[n]
#     ans=min(ans,dist[n]+x/c_limit)

# print(intans)
    

import sys
import heapq
INT_MAX=sys.maxsize
ans=INT_MAX
n, m, x = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
c_list=set()
# Please write your code here.
graph=[[] for _ in range(n+1)] 
for i,j,l,c in edges:
    c_list.add(c)
    graph[i].append((j,l,c))
    graph[j].append((i,l,c))

for c_limit in c_list:
    dist=[INT_MAX]*(n+1)
    dist[1]=0
    pq=[]
    heapq.heappush(pq,(0,1))
    while pq:
        c_dist, c_node= heapq.heappop(pq)
        if dist[c_node]!=c_dist : continue 
        for n_node, n_l,n_c in graph[c_node]:
            if n_c < c_limit : continue 
            if dist[n_node] > n_l+c_dist:
                dist[n_node]= n_l+c_dist
                heapq.heappush(pq,(dist[n_node],n_node))
    B=dist[n]
    A= c_limit 
    ans=min(ans, B+x/A)

print(int(ans))