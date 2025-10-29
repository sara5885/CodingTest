#251029 (17:49)
import heapq 
n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
total_cost=0
while len(arr)>1:
    # arr.sort()
    # min1=arr[0]
    # min2=arr[1]
    min1=heapq.heappop(arr)
    min2=heapq.heappop(arr)
    # print(min1,min2)
    total_cost+=(min1+min2)
    
    heapq.heappush(arr,min1+min2)

print(total_cost)