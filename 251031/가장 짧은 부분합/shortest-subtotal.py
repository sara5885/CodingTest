#251031 (16:59)
import sys 
INT_MAX=sys.maxsize 
n, s = map(int, input().split())
arr = [0]+list(map(int, input().split()))

ans=INT_MAX 

sum_val=0
j=0
for i in range(1,n+1):
    while j+1<=n and sum_val<s:
        sum_val+=arr[j+1]
        j+=1 
    if sum_val<s:
        break 
    ans=min(ans,j-i+1)
    sum_val-=arr[i] #다시 처음부터 매번 더하는게 아니라 sum_val에서 뒤에 추가하고 맨앞삭제하고 


if ans==INT_MAX:
    ans=-1 
print(ans)