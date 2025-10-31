#251031 (14:12)
N, K, B = map(int, input().split())
missing = [int(input()) for _ in range(B)]

exist=[0]*(N+1)
for i in range(1,N+1):
    if i not in missing:
        exist[i]=1 
max_cnt=0
for i in range(1,N+2-K):
    if sum(exist[i:i+K])>max_cnt:
        max_cnt=sum(exist[i:i+K])
        # print(i)
        # print(exist[i:i+K])
        # print(max_cnt)
print(K-max_cnt)


# prefix_sum=[0]*(N+1)
# for i in range(1,N+1):
#     if i not in missing:
#         prefix_sum[i]=prefix_sum[i-1]+1
#     else:
#         prefix_sum[i]=prefix_sum[i-1]
