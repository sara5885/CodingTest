from collections import deque
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

neighbor=[[] for _ in range(n+1) ] 
indegree=[0]*(n+1)
for a,b in edges: 
    neighbor[a].append(b)
    indegree[b]+=1 

pq=deque()
pq_cnt=0
for i in range(1,n+1):
    if indegree[i]==0: 
        pq.append(i)
        pq_cnt+=1 

cons=True
while pq:
    node=pq.popleft()
    for neigh in neighbor[node]:
        if indegree[neigh]==0: 
            cons=False
            break 
        indegree[neigh]-=1 
        if indegree[neigh]==0: 
            pq.append(neigh)
            pq_cnt+=1 

    if not cons: break 

if pq_cnt!=n: cons=False

if cons : print("Consistent")
else: print("Inconsistent")
            


