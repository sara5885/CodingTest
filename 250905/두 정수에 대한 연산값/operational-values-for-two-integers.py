a, b = map(int, input().split())

# Please write your code here.
def compute_num(a,b):
    tmp1=max(a,b)+25
    tmp2=min(a,b)*2
    if a>b:
        return(tmp1,tmp2)
    else:
        return(tmp2,tmp1)

c,d=compute_num(a,b)
print(c,d)