n = int(input())
arr = list(map(int, input().split()))

def change_arr(arr):
    for i in range(len(arr)):
        arr[i]=abs(arr[i])

change_arr(arr)
for i in arr:
    print(i,end=" ")