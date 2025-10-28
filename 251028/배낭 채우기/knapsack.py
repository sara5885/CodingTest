# 251028 (20:54)

N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# dp[i] : 무게 합이 i일 때 가치 최대 
# dp[0]:
dp=[-1]*(M+1) 
dp[0]=0 
for i in range(N):
    for j in range(M,-1,-1):
        if j>=w[i] and dp[j-w[i]]!=-1:
            dp[j]=max(dp[j], dp[j-w[i]]+v[i])

max_val=0

for val in dp:
    max_val=max(max_val,val)
print(max_val)