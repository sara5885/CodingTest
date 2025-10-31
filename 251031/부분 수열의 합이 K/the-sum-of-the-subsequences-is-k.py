# 251031 (13:56)
n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum=[0]*(n+1)

for i in range(1,n+1):
    prefix_sum[i]=prefix_sum[i-1]+arr[i-1]

# print(prefix_sum)
ans=0
for i in range(n):
    for j in range(i,n+1):
        # print(prefix_sum[j],prefix_sum[i], i,j)
        if prefix_sum[j]-prefix_sum[i] == k:
            ans+=1

print(ans)