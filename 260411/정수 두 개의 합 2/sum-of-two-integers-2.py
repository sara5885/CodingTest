n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ans=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]<=k:
            ans+=1 
print(ans)
