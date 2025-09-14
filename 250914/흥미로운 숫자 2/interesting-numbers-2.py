# 250914 (15:14) (15:48)
X, Y = map(int, input().split())

# 흥미로운 숫자
# 자릿수_arr 만들기 : 
# 자릿수_arr => len(arr)==2 and 하나는 값이 1이고 나머지는 1보다 커야함 

cnt=0
for i in range(X,Y+1):
    num_arr=str(i)
    base_arr=[0]*10
    for j in range(len(str(i))):
        base_arr[int(num_arr[j])]+=1
    cnt_arr=[x for x in base_arr if x!=0]
    if len(cnt_arr)!=2:
        continue 
    elif (cnt_arr[0]==1 and cnt_arr[1]>=1) or (cnt_arr[1]==1 and cnt_arr[0]>=1):
        cnt+=1
    # refine_arr=[(index,value) for index,value in enumerate(cnt_arr) if value!=0]

    # if len(refine_arr)!=2:
    #     continue 
    # else:
    #     if refine_arr

print(cnt)