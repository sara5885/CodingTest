n = int(input())

# Please write your code here.

def rec1(n):
    if n==0:
        return 
    print(n, end=" ")
    rec1(n-1)
def rec2(n):
    if n==0:
        return 
    rec2(n-1)
    print(n,end=" ")


rec2(n)
print()
rec1(n)