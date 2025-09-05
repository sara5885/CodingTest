n = int(input())

# Please write your code here.
cnt =0
def compute_num(num):
    global cnt 
    if num==1:
        return cnt 
    cnt+=1
    if num%2==0:
        return compute_num(num//2)
    elif num%2==1:
        return compute_num(num*3+1)

print(compute_num(n))