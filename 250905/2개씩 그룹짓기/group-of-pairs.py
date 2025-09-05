n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
max_num=0
for i in range(n):
    tmp=nums[i]+nums[2*n-i-1]
    if tmp>max_num:
        max_num=tmp 

print(max_num)