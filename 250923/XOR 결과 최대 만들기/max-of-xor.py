# 250923 (01:09)
n, m = map(int, input().split())
A = list(map(int, input().split()))

max_xor=0
def find_max_xor(index,count,current_num):
    global max_xor
    if count==m:
        max_xor=max(max_xor,current_num)
        return 
    if index==n: # 조합 못채웠는데 이미 마지막 index인 애들 
        return 
    
    find_max_xor(index+1,count,current_num)
    find_max_xor(index+1,count+1, current_num=current_num^A[index])
find_max_xor(0,0,0)
print(max_xor)