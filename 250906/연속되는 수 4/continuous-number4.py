n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt=1
max_cnt=1

for i in range(1,n):
    if arr[i]>arr[i-1]:
        cnt+=1
    else:
        max_cnt=max(cnt,max_cnt)
        cnt=1

max_cnt=max(cnt,max_cnt)
print(max_cnt)