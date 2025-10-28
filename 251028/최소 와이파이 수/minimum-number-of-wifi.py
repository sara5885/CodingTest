#251028 (22:22)
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 1 1 0 1 1 1 
# 거리 1 
# 사람 살고있으면 거기서 +m에 wifi 놓기 / wifi 놓은 지점 +m에서 다시시작 
cnt,i=0,0 
while i<n:
    if arr[i]==1:
        cnt+=1
        i+=2*m+1
    else:
        i+=1 
print(cnt)