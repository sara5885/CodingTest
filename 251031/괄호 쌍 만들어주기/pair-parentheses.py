# 251031 (16:07)
A = input()

# ((( )))
r=[0]*(len(A))
cnt=0
for i in range(len(A)-2,-1,-1):
    if A[i]==')' and A[i+1]==')':
        r[i]=r[i+1]+1 
    else:
        r[i]=r[i+1]

case=0
for i in range(1,len(A)-1):
    if A[i-1]=='(' and A[i]=='(' :
        case+=r[i+1]

print(case)