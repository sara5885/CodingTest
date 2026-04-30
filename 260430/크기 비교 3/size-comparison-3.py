import heapq 
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

adjacent=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
for a,b in edges:
    adjacent[a].append(b)
    indegree[b]+=1 

pq=[]
for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(pq, i)

while pq:
    node=heapq.heappop(pq)
    print(node,end=" ")
    for neigh in adjacent[node]:
        indegree[neigh]-=1
        if indegree[neigh]==0:
            heapq.heappush(pq,neigh)

