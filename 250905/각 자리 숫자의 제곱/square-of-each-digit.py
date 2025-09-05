N = int(input())

# Please write your code here.
def print_sum(N):
    if N<10:
        return N*N
    tmp=N%10
    return print_sum(N//10)+tmp*tmp 

print(print_sum(N))