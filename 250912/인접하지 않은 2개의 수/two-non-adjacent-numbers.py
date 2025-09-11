n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max_sum=0

for i in range(0,n-2):
    for j in range(i+2, n):
        max_sum=max(max_sum, numbers[i]+numbers[j])
print(max_sum)