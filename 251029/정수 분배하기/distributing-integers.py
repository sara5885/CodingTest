# 251029 (14:22)
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 같은 크기의 정수 k 를 m개 만들기 
arr.sort()
right=arr[-1]
left=1 

ans=0

def check_possible(x):
    cnt=0
    for a in arr:
        cnt+=a//x 
    if cnt>=m:
        return True 
    else:
        return False 

while left<=right:
    mid=(right+left)//2 
    if check_possible(mid):
        left=mid+1 
        ans=max(ans,mid)
    else:
        right=mid-1 

print(ans)