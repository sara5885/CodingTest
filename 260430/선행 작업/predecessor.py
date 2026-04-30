from collections import deque 
n = int(input())
time = [-1]
prereq_count = [-1]
prereq = [-1]
adjacent=[[] for _ in range(n+1)]
indegree=[0]*(n+1)

for i in range(1,n+1):
    line = list(map(int, input().split()))
    time.append(line[0])
    prereq_count.append(line[1])
    prereq.append(line[2:])
    for j in prereq[i]:
        adjacent[j].append(i)
        indegree[i]+=1


# Please write your code here.
dp=[0]*(n+1)
pq=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        pq.append(i)
        dp[i]+=time[i]

while pq:
    node=pq.popleft()
    for neigh in adjacent[node]:
        dp[neigh]=max(dp[neigh],dp[node])
        indegree[neigh]-=1
        if indegree[neigh]==0:
            dp[neigh]+=time[neigh]
            pq.append(neigh)

print(max(dp))

