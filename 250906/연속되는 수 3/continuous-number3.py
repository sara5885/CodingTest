N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
cnt=1
max_cnt=1
for i in range(N):
    # continue 
    if i!=0 and arr[i]*arr[i-1]>0:
        cnt+=1
    # update (initialization)
    elif i!=0 and arr[i]*arr[i-1]<0:
        max_cnt=max(cnt,max_cnt)
        cnt=1

max_cnt=max(cnt,max_cnt)

print(max_cnt)