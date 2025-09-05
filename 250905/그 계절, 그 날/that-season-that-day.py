Y, M, D = map(int, input().split())
arr_31=[1,3,5,7,8,10,12]
arr_30=[4,6,8,11]
# Please write your code here.
def check_yoonyear(Y):
    if Y%4==0:
        return True
    if Y%4==0 and Y%100==0:
        return False 
    if Y%4==0 and Y%400==0:
        return True 
    return False 
def check_date(Y,M,D):
    if M==2:
        if check_yoonyear(Y):
            if D>29:
                return False 
        elif D>28:
                return False 
    if M in arr_30 and D>30:
        return False 
    return True 
def check_season(Y,M,D):
    if check_date(Y,M,D):
        if M>=3 and M<=5 :
            return "Spring"
        if M>=6 and M<=8:
            return "Summer"
        if M>=9 and M<=11:
            return "Fall"
        if M>=12 or M<=2:
            return "Winter"
    else:
        return -1 

print(check_season(Y,M,D))