n = int(input())

def check_number(n):
    return n%2==0 and (n//10+n%10)%5==0

if check_number(n):
    print('Yes')
else :
    print('No')