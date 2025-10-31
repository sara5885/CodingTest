#251031 (16:59)
import sys 
INT_MAX=sys.maxsize 
n, s = map(int, input().split())
arr = [0]+list(map(int, input().split()))

ans=INT_MAX 


sum_val=0
j=1
for i in range(1,n+1):
    while j<=n and sum_val<s:
        sum_val+=arr[j]
        j+=1 
    if sum_val<s:
        break 
    ans=min(j-i,ans)
    sum_val-=arr[i]
if ans==INT_MAX:
    ans=-1 
print(ans)