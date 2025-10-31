#251031 (14:12)
N, K, B = map(int, input().split())
missing = [int(input()) for _ in range(B)]

exist=[0]*(N+1)
for i in range(1,N+1):
    if i not in missing:
        exist[i]=1 
max_cnt=0
prefix_sum=[0]*(N+1)
for i in range(1,N+1):
    prefix_sum[i]=prefix_sum[i-1]+exist[i]
for i in range(1,N+2-K):
    j=i+K-1
    current_sum=prefix_sum[j]-prefix_sum[i-1]
    if current_sum>max_cnt:
        max_cnt=current_sum
print(K-max_cnt)


# prefix_sum=[0]*(N+1)
# for i in range(1,N+1):
#     if i not in missing:
#         prefix_sum[i]=prefix_sum[i-1]+1
#     else:
#         prefix_sum[i]=prefix_sum[i-1]
