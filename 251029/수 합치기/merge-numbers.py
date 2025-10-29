#251029 (17:49)
n = int(input())
arr = list(map(int, input().split()))

total_cost=0
while len(arr)>1:
    arr.sort()
    min1=arr[0]
    min2=arr[1]
    total_cost+=(min1+min2)
    arr.append(min1+min2)
    del arr[0]
    del arr[1]

print(total_cost)