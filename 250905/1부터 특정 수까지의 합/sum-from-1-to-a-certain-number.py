n = int(input())

# Please write your code here.

def answer(n):
    num=0
    for i in range(n+1):
        num+=i 
    return num//10

print(answer(n))

