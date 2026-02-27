import heapq 
n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
ans=0 
while len(arr)>1:
    n1=heapq.heappop(arr)
    n2=heapq.heappop(arr)
    ans+=n1+n2 
    heapq.heappush(arr, n1+n2)
print(ans)