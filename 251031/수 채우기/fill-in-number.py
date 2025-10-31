#251031 (12:32)
n = int(input())
ans=0
max_num=n//5 

for i in range(max_num,-1,-1):
    tmp_num=n
    remainder=tmp_num-(i*5)
    if remainder%2==0:
        ans=i+remainder//2
        break 

if ans==0:
    print(-1)
else:
    print(ans)