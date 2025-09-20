#250920 (16:36) (16:45)
n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))


dict={}

for i in arr:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1


for i in range(m):
    if nums[i] in dict :
        print(dict[nums[i]],end=" ")
    else:
        print(0,end=" ")
