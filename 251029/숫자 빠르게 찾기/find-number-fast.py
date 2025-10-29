#251029 (22:51)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]


for i in range(m):
    target=queries[i]
    left=0
    right=n-1 
    idx=-1
    while left<=right:
        mid=(left+right)//2 
        if arr[mid]==target:
            idx=mid+1
            break 
        elif arr[mid]<target:
            left=mid+1 
        else:
            right=mid-1 
    print(idx)