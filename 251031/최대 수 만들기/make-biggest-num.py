#251031 (12:26)
from functools import cmp_to_key 
n = int(input())
arr = [(input()) for _ in range(n)]

def compare(x,y):
    if int(x[0])<int(y[0]):
        return 1
    elif int(x[0])>int(y[0]):
        return -1 
    else:
        tmp1=x+y
        tmp2=y+x 
        if int(tmp1)>int(tmp2):
            return -1 
        else:
            return 1 

arr.sort(key=cmp_to_key(compare))
for a in arr:
    print(a,end="")