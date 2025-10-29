# 251029 (14:11)
s = int(input())

max_num=s//2 
# n : (1-max_num)
ans=-1
left,right=1,max_num
while left<=right:
    mid = (left+right)//2 
    if mid*(mid+1)/2 <= s:
        ans=max(ans,mid)
        left=mid+1
    else:
        right=mid-1
    
print(ans)