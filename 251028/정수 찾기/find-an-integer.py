n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

set1=set(a)

for i in b:
    if i in set1:
        print(1)
    else:
        print(0)
