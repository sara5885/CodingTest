n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max_num=arr[n-1]
def find_max(num):
    global max_num
    max_num=max(max_num,arr[num])
    if num==0:
        return max_num
    #print(num, max_num)
    return find_max(num-1)

print(find_max(n-1))