#251029 (11:14)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# cutom-lower+1 



for q in queries:
    target=q
    custom_idx=-1 
    lower_idx=n
    left,right=0,n-1 

    while left<=right:
        mid=(left+right)//2 
        if arr[mid]>=target:
            lower_idx=min(lower_idx,mid)
            right=mid-1
        else:
            left=mid+1
    left,right=0,n-1 
    
    while left<=right:
        mid=(left+right)//2 
        if arr[mid]<=target:
            custom_idx=max(custom_idx,mid)
            left=mid+1
        else:
            right=mid-1
    # print(lower_idx,custom_idx)
    if custom_idx<lower_idx:
        print(0)
    else:
        print(custom_idx-lower_idx+1)