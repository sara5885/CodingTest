# # 251209 (12:53)
# import sys 
# INT_MAX=sys.maxsize 
# A = input()
# B = input()
# n=len(A)
# m=len(B)


# dp=[[0 for _ in range(m)] for _ in range(n)] #AXB
# if A[0]==B[0]:
#     dp[0][0]=1
# else:
#     dp[0][0]=2 

# # 최상단 
# for i in range(1,m):
#     if A[0]==B[i]:
#         dp[0][i]=i+1
#     else:
#         dp[0][i-1]=dp[0][i-1]+1
# for i in range(1,n):
#     if B[0]==A[i]:
#         dp[i][0]=i+1
#     else:
#         dp[i][0]=dp[i-1][0]+1 

# # for i in dp:
# #     for j in i:
# #         print(j,end=" ")
# #     print()
# # print()

# for i in range(1,n):
#     for j in range(1,m):
#         if A[i]==B[j]:
#             dp[i][j]=dp[i-1][j-1]+1
#         else:
#             dp[i][j]=min(dp[i-1][j], dp[i][j-1])+1 

# for i in dp:
#     for j in i:
#         print(j,end=" ")
#     print()
# print()
# print(dp[-1][-1])


A = input()
B = input()
n=len(A)
m=len(B)
dp=[[0 for _ in range(m)] for _ in range(n)]

if A[0]==B[0]:
    dp[0][0]=1 
for i in range(1,m):
    if B[i]==A[0]:
        dp[0][i]=1
    else:
        dp[0][i]=dp[0][i-1]
for i in range(1,n):
    if A[i]==B[0]:
        dp[i][0]=1 
    else:
        dp[i][0]=dp[i-1][0]

# for i in dp:
#     for j in i:
#         print(j,end=" ")
#     print()
# print()
for i in range(1,n):
    for j in range(1,m):
        if A[i]==B[j]:
            # dp[i][j]=dp[i-1][j-1]+1
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

# for i in dp:
#     for j in i:
#         print(j,end=" ")
#     print()
# print()

print(dp[-1][-1])