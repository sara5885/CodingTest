# 251028 (21:59)
n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

# set1=set(arr1)
# set2=set(arr2)

# same_flag=True 
# for x in set1:
#     if x not in set2:
#         same_flag=False 
#         break
# for x in set2:
#     if x not in set1:
#         same_flag=False 
#         break 
    

for x in arr2:
    if x in arr1:
        print(1,end=" ")
    else:
        print(0,end=" ")