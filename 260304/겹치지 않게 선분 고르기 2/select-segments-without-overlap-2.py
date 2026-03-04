n = int(input())
x1, x2 = [], []
segments=[]
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)
    segments.append((a,b))

segments.sort()
# for i in segments:
#     for j in i:
#         print(j,end=" ")
#     print()

dp=[0]*(n)

for i in range(n):
    dp[i]=1
    for j in range(i):
        # dp[i] : segments[i]
        # segments[j][0], segments[j][1] : 이전 선분의 시작 / 끝 
        # segments[i][0], segments[i][1]
        if segments[i][0] > segments[j][1]: 
            dp[i]=max(dp[i], dp[j]+1)

print(max(dp))
