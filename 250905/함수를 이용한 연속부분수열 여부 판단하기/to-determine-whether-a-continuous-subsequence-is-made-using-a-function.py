n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_con_part(a,b):
    # ex) [1,7,2,8], [7,2]
    for i in range(len(a)-len(b)+1): # i : idx of a
        for j in range(len(b)): #j:idx of b 
            if (b[j]!=a[j+i]):
                break
            if j==len(b)-1:
                return True 
    return False 
if is_con_part(a,b):
    print('Yes')
else:
    print('No')