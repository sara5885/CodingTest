import sys 
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
INT_MAX=sys.maxsize 
INT_MIN=-sys.maxsize

max_num=INT_MIN

for i in range(n-k+1):
    tmp_num=0
    for j in range(i,i+k):
        tmp_num+=arr[j]
    max_num=max(max_num,tmp_num)

print(max_num)