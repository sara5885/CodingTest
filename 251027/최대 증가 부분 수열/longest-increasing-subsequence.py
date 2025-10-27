# 251027 (23:00) (23:03)
import sys 
INT_MIN=-sys.maxsize 
n = int(input())
m = list(map(int, input().split()))

# dp
# dp[i]= 이전 값들 
# 조건 : arr[i] > arr[j] 
# dp
dp=[1]*(n)
# dp[0]=1 
for i in range(1,n):
    for j in range(0,i):
        if m[i]>m[j]:
            dp[i]=max(dp[i],dp[j]+1)

ans=0
for i in range(n):
    ans=max(dp[i],ans)
# print(dp)
print(ans)