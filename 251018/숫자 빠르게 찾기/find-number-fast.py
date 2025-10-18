# 251018 (19:01)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

for num in queries:
    # num 
    left,right=0, n-1 
    find_flag=False 
    while left<=right:
        mid=(left+right)//2 
        if arr[mid]==num:
            print(mid+1)
            find_flag=True 
            break 
        elif arr[mid]>num:
            right=mid-1 
        else:
            left=mid+1

    if find_flag==False :
        print(-1)

