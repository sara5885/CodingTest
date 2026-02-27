n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans=0 
while len(arr)>1:
    arr.sort()
    new_num=arr[0]+arr[1]
    ans+=new_num
    new_arr=arr[2:]
    new_arr.append(new_num)
    arr=new_arr

print(ans)