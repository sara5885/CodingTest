A = input()

# Please write your code here.
def check_arr(A):
    new_arr=[]
    for i in range(len(A)):
        if A[i] not in new_arr:
            new_arr.append(A[i])
    if len(new_arr)>=2:
        return "Yes"
    else:
        return "No"

print(check_arr(A))