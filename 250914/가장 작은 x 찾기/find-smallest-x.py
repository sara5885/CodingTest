# 250914 (17:21)

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

min_answer=10001
for i in range(10000):
    tmp_num=i*2
    satisfied=True 
    for j in range(len(ranges)):# 2곱하는 거 계속 진행해보기 
        if tmp_num>=a[j] and tmp_num<=b[j]:
            tmp_num*=2 
        else:
            satisfied=False 
            break 
    if satisfied==True :
        min_answer=min(min_answer,i)

print(min_answer)