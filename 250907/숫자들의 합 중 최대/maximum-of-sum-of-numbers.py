import sys 
X, Y = map(int, input().split())

max_sum=-sys.maxsize 
for i in range(X,Y+1):
    tmp_sum=0
    num_arr=list(str(i))
    for j in range(len(num_arr)):
        tmp_sum+=int(num_arr[j])
    max_sum=max(max_sum,tmp_sum)

print(max_sum)