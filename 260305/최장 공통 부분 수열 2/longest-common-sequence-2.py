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


cx,cy = len(A)-1, len(B)-1
while cx!=-1 and cy!=-1 :
    # if dp[cx][cy]==cnt :
    if A[cx]==B[cy]:
        # print(cnt, dp[cx][cy])
        cnt-=1
        arr.append(A[cx])
    cx,cy=dp_loc[cx][cy]
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end="")