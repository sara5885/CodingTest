# 250920 (13:06)
n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

total=l+r+d 
m=len(total)
t%=m 
arr=[0]*m
for i in range(t):
    arr[(i+t)%m]=arr[i]
l=arr[:n]
r=arr[n:2*n]
d=arr[2*n:]
print(*l)
print(*r)
print(*d)