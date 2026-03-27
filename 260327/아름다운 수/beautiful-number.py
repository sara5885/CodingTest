n = int(input())

answer=[]
cnt=0
def check(): #여기가 핵심 
    # 4가지 수 
    idx=0
    while idx<n: #현재위치 
        # 현재위치의 숫자 파악 
        if idx+answer[idx]-1>=n: #out of range 
            return False  

        for j in range(idx,idx+answer[idx]):
            if answer[idx]!=answer[j]:
                return False 
        idx+=answer[idx] #해당 거리만큼 idx에서 점프 
    # print(*answer)
    return True 


def choose(idx):
    global cnt 
    if idx==n+1:
        if check():
            cnt+=1 
        return 
    for i in range(1,5):
        answer.append(i)
        choose(idx+1)
        answer.pop()


choose(1)
print(cnt)