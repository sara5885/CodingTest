n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
R=[0]*n 
# dict에 값 저장 ?
latest_idx=dict()
for i in range(n-1,-1,-1):
    if arr[i] not in latest_idx:
        R[i]=-1 
    else:
        R[i]=latest_idx[arr[i]]
        latest_idx[arr[i]]=i 

ans=-1 
for i in range(n):
    if R[i]!=-1 and R[i]-i<=k:
        ans=max(ans,arr[i])

print(ans )