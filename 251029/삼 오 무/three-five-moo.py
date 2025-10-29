# 251029 (14:31)

n = int(input())

def count_num(x):
    moo=x//3+x//5-x//15 
    return x-moo 

left=1
right=1000000000
min_idx=1000000000

while left<=right: 
    mid=(left+right)//2 
    # print(mid,count_num(mid))
    if count_num(mid)>=n:
        min_idx=min(min_idx,mid)
        right=mid-1
    else:
        left=mid+1 
print(min_idx)