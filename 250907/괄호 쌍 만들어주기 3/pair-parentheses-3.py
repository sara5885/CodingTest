A = input()

# Please write your code here.
cnt=0
for i in range(len(A)):
    if A[i]=='(':
        for j in range(i+1,len(A)):
            if A[j]==')':
                cnt+=1
    else: 
        continue 
print(cnt)