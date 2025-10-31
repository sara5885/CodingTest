#251031 (13:05)
N = int(input())
B = [int(input()) for _ in range(N)]
arr=list(range(1,2*N+1))
for i in range(N):
    arr.remove(B[i])
score=0
for i in range(N):
    b_value=B[i]
    a_value=0
    for j in range(len(arr)):
        if arr[j]>b_value:
            score+=1 
            a_value=arr[j]
            break 
    if a_value==0:
        arr.pop(0)
    else:
        arr.remove(a_value)
        
print(score)