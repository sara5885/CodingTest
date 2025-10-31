# 251031 (16:18)
from sortedcontainers import SortedSet 
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
num=SortedSet()
for i in range(0,n-k):
    if arr[i]==arr[i+k]:
        for j in range(i,i+k+1):
            num.add(arr[j])
print(num[-1])