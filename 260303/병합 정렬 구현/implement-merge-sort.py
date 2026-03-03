# merge sort 

n = int(input())
arr = list(map(int, input().split()))

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2 
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    i,j=0,0
    new_arr=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            new_arr.append(left[i])
            i+=1
        else:
            new_arr.append(right[j])
            j+=1 

    new_arr+=left[i:]
    new_arr+=right[j:]
    return new_arr 
ans=merge_sort(arr)

for an in ans:
    print(an,end=" ")