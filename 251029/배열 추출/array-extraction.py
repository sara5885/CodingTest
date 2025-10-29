#251029 (19:16)
import heapq 
n = int(input())
x = [int(input()) for _ in range(n)]

pq=[]

for i in x:
    if i==0:
        if len(pq)==0:
            print(0)
        else:
            tmp=heapq.heappop(pq)
            print(-tmp)
    else:
        heapq.heappush(pq,(-i))