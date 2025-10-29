#251029 (19:10)
import heapq 
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

pq=[]
for x,y in points:
    heapq.heappush(pq,(x+y,x,y))

for i in range(m):
    _,x,y=heapq.heappop(pq)
    heapq.heappush(pq,(x+y+4,x+2,y+2))
    # print(pq)

_,x,y=heapq.heappop(pq)
print(x,y)