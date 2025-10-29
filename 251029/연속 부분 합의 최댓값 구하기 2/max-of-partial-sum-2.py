import sys
INT_MAX=sys.maxsize 
n = int(input())
a = list(map(int, input().split()))

ans=-INT_MAX
current_sum=0
for i in a:
    if current_sum <0: #이전의 결과값을 기반으로 확인하기. 
        current_sum=i  #그냥 a부터 다시 초기화 
    else:
        current_sum+=i 
    ans=max(ans, current_sum)

print(ans)