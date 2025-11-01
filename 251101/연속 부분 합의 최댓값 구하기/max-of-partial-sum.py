import sys 
INT_MIN=-sys.maxsize 
n = int(input())
arr = list(map(int, input().split()))

dp=[INT_MIN]*(n)
dp[0]=arr[0]

for i in range(1,n):
    dp[i]=max(arr[i], dp[i-1]+arr[i])

ans=INT_MIN
for i in range(1,n):
    ans=max(ans,dp[i])

print(ans)