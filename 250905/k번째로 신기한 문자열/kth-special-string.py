n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
tmp_arr=[]
# Please write your code here.
for i in str:
   #if t in i:
    is_in=True 
    for j in range(len(t)):
        if t[j]!=i[j]:
            is_in=False 
            break
    if is_in:
        tmp_arr.append(i)

tmp_arr.sort()

print(tmp_arr[k-1])

