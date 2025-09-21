#250921 (13:15) (13:17)
import heapq 
n = int(input())
x = [int(input()) for _ in range(n)]
pq=[]
for i in range(n):
    if x[i]==0:
        if pq:
            print(pq[0])
            heapq.heappop(pq)
        else:
            print(0)
    else:
        heapq.heappush(pq,x[i])