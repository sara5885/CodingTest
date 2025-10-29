# 251029 (14:31) (15:34)
import sys 
INT_MAX=sys.maxsize 
n = int(input())

def count_num(x):
    moo=x//3+x//5-x//15 
    return x-moo 

left=1
right=INT_MAX
min_idx=INT_MAX

while left<=right: 
    mid=(left+right)//2 
    # print(mid,count_num(mid))
    if count_num(mid)>=n:
        min_idx=min(min_idx,mid)
        right=mid-1
    else:
        left=mid+1 
print(min_idx)