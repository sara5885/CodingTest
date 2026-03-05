#260305 (16:38)
import sys 
INT_MAX=sys.maxsize 
A = input()
B = input()

dp=[[0 for _ in range(len(B))] for _ in range(len(A))]
arr=[]

dp_loc=[[(-1,-1) for _ in range(len(B))] for _ in range(len(A))]
if A[0]==B[0]: 
    dp[0][0]=1 

for i in range(1,len(A)):
    if B[0]!=A[i]: 
        dp[i][0]=dp[i-1][0]
        dp_loc[i][0]=(i-1,0)
    else:
        dp[i][0]=1
        
        # arr.append(B[0])

for i in range(1,len(B)):
    if A[0]!=B[i]:
        dp[0][i]=dp[0][i-1]
        dp_loc[0][i]=(0,i-1)
    else:
        dp[0][i]=1 
        # dp_str[0][i]=A[0]
        # arr.append(A[0])


for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i]==B[j]:
            dp[i][j]=dp[i-1][j-1]+1
            # arr.append(A[i])
            dp_loc[i][j]=(i-1,j-1)
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            if dp[i-1][j]>dp[i][j-1]:
                dp_loc[i][j]=(i-1,j)
            else:
                dp_loc[i][j]=(i,j-1)

# print(arr)
cnt = dp[-1][-1]

# for row in dp:
#     for col in row:
#         print(col,end=" ")
#     print()

# for row in dp_loc:
#     for r,c in row:
#         print("(",r,c,")",end=" ")
#     print()

# for c in range(1,cnt+1):
#     found=False 
#     for i in range(len(A)):
#         for j in range(len(B)):
#             if dp[i][j]==c and A[i]==B[j]: 
#                 print(i,j, dp[i][j], A[i],B[j] )
#                 arr.append(A[i])
#                 found=True 
#                 break 
#         if found : break 

cx,cy = -1,-1 
while cnt>0:
    if dp[cx][cy]==cnt :
        # print(cnt, dp[cx][cy])
        cnt-=1
        arr.append(A[cx])
        cx,cy=dp_loc[cx][cy]
arr.reverse()
for a in arr:
    print(a,end="")