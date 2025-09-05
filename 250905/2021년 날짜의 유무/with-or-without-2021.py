M, D = map(int, input().split())
arr_31=[1,3,5,7,8,10,12]
arr_30=[4,6,9,11]
def is_date(M,D):
    if M>12:
        return False 
    if M in arr_31:
        if D>31:
            return False 
    if M in arr_30:
        if D>30:
            return False 
    if M==2 :
        if D>28:
            return False 
    return True

if is_date(M,D):
    print('Yes')
else:
    print('No')