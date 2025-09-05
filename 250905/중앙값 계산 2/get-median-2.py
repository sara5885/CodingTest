n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(len(arr)):
    if (i+1)%2==1:
        tmp_arr=sorted(arr[:i+1])
        print(tmp_arr[i//2],end=" ")