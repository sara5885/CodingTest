#251029 (19:19)
import heapq 
n = int(input())
arr = list(map(int, input().split()))

pq=[]
for a in arr:
    heapq.heappush(pq,-a)

while len(pq)>1:
    tmp1=-heapq.heappop(pq)
    tmp2=-heapq.heappop(pq)
    if tmp1==tmp2:
        continue 
    heapq.heappush(pq,-(tmp1-tmp2))

if len(pq)==1:
    print(-pq[0])
else:
    print(-1)