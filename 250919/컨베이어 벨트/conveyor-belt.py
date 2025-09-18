# 250919 (02:53) 
n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))
d=d[::-1]
# up : right ->
# down : <- left 

# 123
# 651 (156)

# 112
# 365 (563)

for i in range(t):
    up_temp=u[-1] #up_temp=>down[-1]
    down_temp=d[0] #down_temp=>up[0]
    for j in range(n-1,0,-1):
        u[j]=u[j-1]
    for j in range(0,n-1,1):
        d[j]=d[j+1]
    d[-1]=up_temp
    u[0]=down_temp
d=d[::-1]
for i in u:
    print(i,end=" ")
print()
for i in d:
    print(i,end=" ")

# 1 2 3
# 6 5 1 

# ? 1 2 (3)
# 