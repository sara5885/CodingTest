# 251029 (11:45)
n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# binary search 
# : target에 대한 bound 각각 logN에 구할 수 있음 

# segment : a-b : lowerbound(a) - upperbound(b)
# 이 두 차이를 구하려면 upperbound는 target보다 큰 가장 작은 idx임 
points.sort() 
def upper_bound(x):
    left,right=0,n-1 
    upper_idx=n
    while left<=right:
        mid=(left+right)//2 
        if points[mid]>x:
            upper_idx=min(upper_idx,mid)
            right=mid-1
        else:
            left=mid+1 
    return upper_idx

def lower_bound(x):
    left,right=0,n-1 
    lower_idx=n 
    while left<=right:
        mid=(left+right)//2 
        if points[mid]>=x:
            right=mid-1 
            lower_idx=min(lower_idx,mid)
        else:
            left=mid+1 
    return lower_idx

for s,e in segments:
    count=upper_bound(e)-lower_bound(s) #모든 n 볼 필요 없이 arr에 대한 갯수 이미 포함되어있는 것
    print(count)