#250921 (13:07)
import heapq 
pq=[]
n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    heapq.heappush(pq,-arr[i])

for i in range(m):
    tmp=pq[0]
    heapq.heappop(pq)
    heapq.heappush(pq,tmp+1)

print(-pq[0])

