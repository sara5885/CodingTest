n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()
is_same=True 
for i in range(n):
    if A[i]==B[i]:
        continue 
    else:
        is_same=False 
        break 

if is_same:
    print('Yes')
else:
    print('No')