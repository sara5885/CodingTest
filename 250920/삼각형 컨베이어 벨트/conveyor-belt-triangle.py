# 250920 (13:06)
n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
# total_arr=l[:]+r[:]+d[::-1]
total_arr=l[:]+r[:]+d[:]
# 1초 : total_arr=total_arr[-1]+total_arr[:-1]
# 2초 : total_arr=total_arr[-t:]
total_arr=total_arr[-t:]+total_arr[:-t]
l=total_arr[:n]
r=total_arr[n:2*n]
d=total_arr[2*n:]
# d=d[::-1]

for i in l:
    print(i,end=" ")
print()
for i in r:
    print(i,end=" ")
print()
for i in d:
    print(i,end=" ")
