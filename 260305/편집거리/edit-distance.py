# 260305 (14:14)
import sys
INT_MAX=sys.maxsize 
A = input()
B = input()

# dp[i][j] : A의i, B의j까지 고려했을 때 A를 B로 바꾸기 위해 필요한 최소 연산 횟수 
dp=[[INT_MAX for _ in range(len(B)+1)] for _ in range(len(A)+1)]
# 1. 초기조건
# 2. 업데이트
    # i==j : dp[i][j]=dp[i-1][j-1]
    # i!=j : 삽입/삭제/변경 

dp[0][0]=1
for i in range(1, len(A)+1):
    dp[i][0]=i
for i in range(1,len(B)+1):
    dp[0][i]=i

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1]==B[j-1]:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1 

# for row in dp:
#     for col in row:
#         print(col,end=" ")
#     print()

print(dp[-1][-1])