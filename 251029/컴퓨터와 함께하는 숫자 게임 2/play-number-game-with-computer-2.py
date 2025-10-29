#251029 (13:32)
import sys 
INT_MAX=sys.maxsize
m = int(input())
a, b = map(int, input().split())

# 1-M 사이에서 컴퓨터가 A-B의 값 
# 가장 적게 지속될 때 : 한번에 맞춰버림
# A부터 B까지 다 해보기? max_cnt, min_cnt 세기 
max_cnt=0
min_cnt=INT_MAX

# 몇번째에 해당 값이 나오는지 출력 
def count(x): 
    cnt=1
    left,right=1,m
    while left<=right:
        mid=(left+right)//2 
        if mid==x:
            return cnt 
        elif mid<x:
            left=mid+1 
        else:
            right=mid-1 
        cnt+=1 
    return cnt 

for i in range(a,b+1):
    tmp=count(i)
    max_cnt=max(max_cnt,tmp)
    min_cnt=min(min_cnt,tmp)

print(min_cnt,max_cnt)