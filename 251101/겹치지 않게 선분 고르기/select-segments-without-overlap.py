n = int(input())
x1, x2 = [], []
segments=[]
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)
    segments.append([a,b])

segments.sort(key=lambda x:x[1])

cnt =1 
s,e=segments[0][0], segments[0][1]
for i in range(1,len(segments)):
    tmp_s,tmp_e=segments[i]
    if e<tmp_s:
        cnt+=1 
        s,e=tmp_s,tmp_e 
print(cnt)