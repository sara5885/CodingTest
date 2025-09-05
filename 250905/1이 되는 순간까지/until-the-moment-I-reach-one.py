N = int(input())

# Please write your code here.
cnt=0
def num_cnt(N):
    global cnt 
    if N==1:
        return cnt
    if N%2==0:
        cnt+=1
        return num_cnt(N//2)
    elif N%2==1:
        cnt+=1
        return num_cnt(N//3)

print(num_cnt(N))