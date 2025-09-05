n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
answer=0
def compute_arr():
    global m
    global A 
    global answer 
    while m>0:
        answer+=A[m-1]
        if m%2==1:
            m-=1
        else :
            m=int(m/2)
    return answer 

print(compute_arr())