# 260303 (14:11)

n = int(input())
arr = list(map(int, input().split()))

max_len=len(str(max(arr)))
# print(max_len)

for pos in range(1,max_len+1):
    # 자릿수에 맞춰서 넣어주기 
    new_arr=[[] for _ in range(10)]
    for num in arr:
        # 현재 pos랑 비교해서 자릿수보다 작으면 0에 append 
        if len(str(num))<pos:
            new_arr[0].append(num)
        else:
            new_arr[int(str(num)[-pos])].append(num) #현재 자릿수의 값 
    new_new_arr=[]
    for arr in new_arr:
        for num in arr:
            new_new_arr.append(num)
    arr=new_new_arr 

for i in arr:
    print(i,end=" ")