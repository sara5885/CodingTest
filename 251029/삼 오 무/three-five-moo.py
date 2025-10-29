# 251029 (14:31)

n = int(input())

def count_num(x):
    moo=x//3+x//5-x//15 
    return x-moo 

left=1
right=1000000000
mid=0
while left<=right: 
    mid=(left+right)//2 
    # print(mid,count_num(mid))
    if count_num(mid)==n:
        break
    elif count_num(mid)<n:
        left=mid+1 
    else:
        right=mid-1 

print(mid)