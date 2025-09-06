n = int(input())
arr = [int(input()) for _ in range(n)]

max_cnt=0
cnt=1
for i in range(1,n):
    #print('i:',i,'arr[i]:',arr[i], 'cnt:',cnt)
    if arr[i]==arr[i-1]:
        cnt+=1
    else:
        if cnt>max_cnt:
            max_cnt=cnt 
            cnt=1

print(max_cnt)