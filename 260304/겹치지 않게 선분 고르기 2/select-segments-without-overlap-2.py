# 260304 (19:48)
n = int(input())
x1, x2 = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)
max_len=max(x2)

dp=[0]*(max_len+1)

# if 1 in x1:
#     dp[1]=1 

for i in range(1, max_len+1):
    dp[i]=dp[i-1]
    for idx in range(n):
        
        
        # idx번째 x1, x2 => x1[idx], x2[idx]
        # x2[idx]가 i보다 작을 때에만 적용
        if x2[idx]!=i : continue 
        
        dp[i]=max(dp[i], dp[x1[idx]-1]+1)

print(max(dp))
