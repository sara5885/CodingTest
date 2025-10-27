# 251027 (21:25)
n = int(input())


arr=[-1]*(n+1)

def fibbo(n):
    if arr[n]!=-1:
        return arr[n]
    if n==1 or n==2:
        arr[n]=1
        return 1 
    arr[n]=fibbo(n-1)+fibbo(n-2)
    return arr[n]

print(fibbo(n))