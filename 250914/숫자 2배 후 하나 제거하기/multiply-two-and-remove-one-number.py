# 250914 (16:05)
n = int(input())
arr = list(map(int, input().split()))

min_sum=9900

# 1. twice element 
for i in range(n):
    arr[i]*=2 # 이렇게 두배해주면 마지막에 다시 2로 나눠주면 됨 

    # 2. remove element 
    for j in range(n):
        diff_sum=0
        selected_arr=[] #refined array 

        for k in range(n):
            if j==k:
                continue 
            else:
                selected_arr.append(arr[k])
        
        # compute diff sum 
        for k in range(1,len(selected_arr)):
            diff_sum+=(abs(selected_arr[k]-selected_arr[k-1]))
        
        min_sum=min(min_sum,diff_sum)
    arr[i]//=2

print(min_sum)



