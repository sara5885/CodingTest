n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for i in  nums:
    print(i,end=" ")
nums.sort(reverse=True)
print('')
for i in nums:
    print(i, end=" ")