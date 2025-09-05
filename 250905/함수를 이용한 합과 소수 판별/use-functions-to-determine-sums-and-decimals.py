a, b = map(int, input().split())

# Please write your code here.

def is_sosu(n):
    for i in range(2,n):
        if n%i==0:
            return False 
    return True 

def is_sum_even(n):
    if n==100:
        return False 
    elif n>=10:
        return (n//10+n%10)%2==0
    elif n<10:
        return n%2==0


def is_answer(n):
    return is_sosu(n) and is_sum_even(n)

cnt=0
for i in range(a,b+1):
    if is_answer(i):
        cnt+=1
print(cnt)