n = int(input())

answer=[]
cnt=0
def check_cnt():
    global cnt
    num_cnt=[0]*5
    check_flag=True 
    for idx in range(len(answer)):
        num_cnt[idx]+=1 
    for idx in range(1,len(num_cnt)):
        if num_cnt[idx]%idx!=0:
            check_flag=False 
    if check_flag==True:
        print('answer:',answer)
        cnt+=1
    return 
    # answer이 아름다운 수인지 check 

def choose(num):
    if num==n+1:
        check_cnt()
        return 
    for i in range(1,5):
        answer.append(i)
        choose(num+1)
        answer.pop()
    return 

choose(1)
print(cnt)