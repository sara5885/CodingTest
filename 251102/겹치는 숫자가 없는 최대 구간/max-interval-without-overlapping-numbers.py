n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
num=set()
ans=0
j=0
for i in range(n): #0~n-1
    # num.add(arr[i])
    while j<n and arr[j] not in num:
        
        num.add(arr[j])
        j+=1 
    ans=max(ans, j-i) #현재 length는 j-i+1이 됨 
    num.remove(arr[i])

print(ans)