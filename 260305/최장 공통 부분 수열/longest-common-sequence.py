# 260305 (13:43)
A = input()
B = input()

dp=[[0 for _ in range(len(B))] for _ in range(len(A))]
# dp[i][j] : A에서 i번째까지, B에서 J번째까지 문자 고려했을 때 최장 수열 

# 1. 초기조건
# dp[0][0] : 둘이 같으면 1 아니면 0
# dp[0][j] : 둘이 같으면 1, 아니면 0 
for i in range(len(A)):
    if A[i]==B[0]:
        dp[i][0]=1
    else:
        dp[i][0]=0 
for i in range(len(B)):
    if B[i]==A[0]:
        dp[0][i]=1
    else:
        dp[0][i]=0

# for row in dp:
#     for col in row:
#         print(col,end=" ")
#     print()

# 2. dp 채우기 
for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i]==B[j]: 
            dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1)
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

# for row in dp:
#     for col in row:
#         print(col,end=" ")
#     print()

print(dp[-1][-1])