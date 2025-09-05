N = int(input())

# Please write your code here.

def find_num(n):
    if n==1:
        return 1
    if n==2:
        return 2 
    
    return find_num(n-1)+find_num(n//3)


print(find_num(N))