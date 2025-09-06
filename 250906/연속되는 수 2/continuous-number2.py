n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
max_cnt =1
cnt=1 

# case 1 
# for i in range(1,n):
#     if arr[i]!=arr[i-1]:
#         cnt=1
#     else:
#         cnt+=1 
#     # 매번 update 
#     max_cnt=max(max_cnt,cnt)

# print(max_cnt)

# case 2 
for i in range(n):
    if i!=0 and arr[i]!=arr[i-1]:
        max_cnt=max(max_cnt,cnt)
        cnt=1
    elif i!=0:
        cnt+=1 
    # 매번 update 
max_cnt=max(max_cnt,cnt)
print(max_cnt)