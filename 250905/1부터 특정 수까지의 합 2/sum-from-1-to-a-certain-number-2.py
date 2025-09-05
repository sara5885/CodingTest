N = int(input())

# Please write your code here.

def print_sum(N):
    if N==1:
        return 1
    return print_sum(N-1)+N

print(print_sum(N))