N = int(input())

# Please write your code here.
def print_idx(num):
    if num==1:
        return 2
    if num==2:
        return 4
    return (print_idx(num-1)*print_idx(num-2))%100


print(print_idx(N))