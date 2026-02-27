import sys 
INT_MAX=sys.maxsize 
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
idx=0
sum=0
ans=-INT_MAX

for i in a:
    sum+=i
    ans=max(ans,sum)
    if sum<0:
        sum=0 

print(ans)