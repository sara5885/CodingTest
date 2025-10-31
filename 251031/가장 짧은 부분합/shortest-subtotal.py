#251031 (16:59)
n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_dist=100001

for i in range(n-1):
    tmp_sum=arr[i]
    if tmp_sum>=s:
        min_dist=1
        break
    for j in range(i+1,n):
        tmp_sum+=arr[j]
        if tmp_sum>=s:
            min_dist=min(min_dist,j-i+1)
            break 

print(min_dist)