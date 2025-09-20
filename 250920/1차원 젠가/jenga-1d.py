# 250920 (16:01)
n = int(input())
# 1 2 3 1 1 5 
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
s1-=1
e1-=1
s2-=1
e2-=1 
arr=blocks[:s1]+blocks[e1+1:]

arr=arr[:s2]+arr[e2+1:]
print(len(arr))
for i in arr:
    print(i)