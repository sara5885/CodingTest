# 260218 (16:06)
import sys
INT_MAX=sys.maxsize 
A = input()

if len(A)==1:
    print(2)
else:
    ans=INT_MAX 
    tmp_arr=A
    for i in range(1,len(A)): #[1:n-1]~ [n-1:1] 
        # i만큼 shift : 뒤에서부터 i개가 앞으로 온 것 
        tmp_arr2=tmp_arr[-1]+tmp_arr[:len(A)-1]
        tmp_arr=tmp_arr2
        tmp_cnt=1
        new_arr=tmp_arr[0]
        # print(new_arr)
        for j in range(1,len(A)):
            if tmp_arr[j]!=tmp_arr[j-1]: #다름 update 진행
                new_arr=new_arr+str(tmp_cnt)
                new_arr=new_arr+tmp_arr[j]
                tmp_cnt=1
            else: #같음
                tmp_cnt+=1
            # print(new_arr)
        new_arr=new_arr+str(tmp_cnt)
        ans=min(ans,len(new_arr))


    print(ans)