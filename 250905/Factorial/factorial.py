N = int(input())

# Please write your code here.

def fact(N):
    if N==0:
        return 1
    if N==1:
        return 1
    if N==2:
        return 2
    return fact(N-1)*N 

print(fact(N))