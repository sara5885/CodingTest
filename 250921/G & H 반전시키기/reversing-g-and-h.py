#250921 (12:55)
N = int(input())
a = input()
b = input()

cnt=0
for i in range(N):
    if a[i]==b[i]:
        continue 
    else :
        if i==0:
            cnt+=1
        elif a[i]!=b[i] and a[i-1]==b[i-1]: # 다른 시작점 
            cnt+=1 
        else:
            continue 

print(cnt)
