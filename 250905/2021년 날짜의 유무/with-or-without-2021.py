M, D = map(int, input().split())

def is_date(M,D):
    if M>12 :
        return False 
    if D>31:
        return False 
    if M==2 :
        if D>28:
            return False 
    return True

if is_date(M,D):
    print('Yes')
else:
    print('No')