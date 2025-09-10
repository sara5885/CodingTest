n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

max_loc=max(x)
arr=[0]*(max_loc+1)

for i in range(len(x)):
    if c[i]=='G':
        arr[x[i]]=1
    elif c[i]=='H':
        arr[x[i]]=2

max_score=0
for i in range(1,len(arr)-k):
    tmp_score=0
    for j in range(i,i+k+1):
        tmp_score+=arr[j]

    max_score=max(max_score,tmp_score)

print(max_score)


