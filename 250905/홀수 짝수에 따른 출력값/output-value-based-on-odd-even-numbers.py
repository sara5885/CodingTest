N = int(input())

# Please write your code here.
def odd(N):
    if N==1:
        return 1
    return odd(N-2)+N
def even(N):
    if N==0:
        return 0
    if N==2:
        return 2
    return even(N-2)+N 

if N%2==0:
    print(even(N))
else:
    print(odd(N))