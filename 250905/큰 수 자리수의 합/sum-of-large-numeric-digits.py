a, b, c = map(int, input().split())

# Please write your code here.
tmp=a*b*c 
#total_sum=0
def compute_ans(num):
    #global total_sum
    if num<10:
        return num 
    return num%10+compute_ans(num//10)

print(compute_ans(tmp))