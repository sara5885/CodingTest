#251027 (21:28)
n = int(input())

def stair(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n==3:
        return 1 
    return stair(n-2)+stair(n-3)

print(stair(n)%10007)