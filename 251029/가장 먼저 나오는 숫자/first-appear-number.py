# 251029 (11:39)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# 최초 등장 위치 : lower bound 

for q in query:
    left,right=0,n-1 
    lower_idx=n 
    while left<=right:
        mid=(left+right)//2 
        if arr[mid]>=q:
            right=mid-1 
            lower_idx=min(lower_idx,mid)
        else:
            left=mid+1 
    if arr[lower_idx]!=q:
        print(-1)
    else:
        print(lower_idx+1)