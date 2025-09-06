n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
if arr[0]>t:
    cnt=1
else:
    cnt=0 
max_cnt=0

for i in range(1,n):
    if arr[i]>t:
        cnt+=1
    else:
        max_cnt=max(max_cnt,cnt)
        cnt=1

max_cnt=max(max_cnt,cnt)

print(max_cnt)
