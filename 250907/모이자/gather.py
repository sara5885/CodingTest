import sys 
INT_MAX=sys.maxsize
INT_MIN=-sys.maxsize

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_dist=INT_MAX
for i in range(n):
    tmp_dist=0
    for j in range(n):
        tmp_dist+=abs(A[j]*(i-j))
    if min_dist>tmp_dist:
        min_dist=tmp_dist

print(min_dist)