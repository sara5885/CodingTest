# 251029 (15:51)
import sys 
n = int(input())
a = list(map(int, input().split()))

current_sum=a[0]
max_sum=a[0]
for i in range(1,n) :
    current_sum=max(current_sum+a[i],a[i])
    max_sum=max(current_sum,max_sum)

print(max_sum)