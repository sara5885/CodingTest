y = int(input())

def is_yoonyear(year):
    if year%4!=0:
        return False 
    if year%100==0 and year%400!=0:
        return False 
    return True

if is_yoonyear(y):
    print('true')
else:
    print('false')