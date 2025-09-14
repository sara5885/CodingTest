# 250914 (16:24)
N = int(input())
seat_str = str(input())
seat=[int(x) for x in seat_str]
max_diff=0
for i in range(len(seat)):
    if seat[i]!=0:
        continue 
    seat[i]=1 
    print('i, seat:',i,seat)
    # 가장 가까운 거리 계산 
    tmp_dist=30
    cnt=1

    if seat[0]==1:
        flag_1=True 
    else:
        flag_1=False 

    for j in range(1, len(seat)):
        if seat[j]==1: #원래 cnt 있으면 update해주고 다시 초기화 
            if flag_1==True:
                tmp_dist=1
                continue 
            else:
                tmp_dist=min(cnt,tmp_dist)
            cnt=1
            flag_1=True 
        # else : 0이니까 마저 count 
        else :
            flag_1=False 
            cnt+=1 

    max_diff=max(max_diff,tmp_dist)
    seat[i]=0

print(max_diff)