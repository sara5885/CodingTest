a, b = map(int, input().split())

# Please write your code here.

def change_num(a,b):
    tmp1=min(a,b)+10
    tmp2=max(a,b)*2
    if a>b:
        return (tmp2,tmp1)
    else:
        return (tmp1,tmp2)

n,m=change_num(a,b)
print(n,m)