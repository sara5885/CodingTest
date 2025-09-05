n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def for_even(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i]=int(arr[i]/2)

for_even(arr)
for i in arr:
    print(i, end=" ")