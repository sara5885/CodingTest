#251029 (19:23)

import heapq 
n = int(input())
arr = list(map(int, input().split()))
# pq=[]
# heapq.heappush(pq,arr)
# print(pq)
max_average=0
for k in range(1,n-1):
    pq=[]
    for i in range(k,n):
        heapq.heappush(pq,arr[i])
    heapq.heappop(pq)
    tmp_average=0
    for i in pq:
        tmp_average+=i
    tmp_average/=len(pq)
    max_average=max(max_average, tmp_average)

print(f"{max_average:.2f}")