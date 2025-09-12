N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

arr=[]
for i in range(1,N+1):
    arr.append(i)
arr.append(1)
arr.append(2)


cnt=0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            flag=False
            # case 1
            if min((N-abs(i-a1)),abs(i-a1)) <=2 and  min((N-abs(j-b1)),abs(j-b1)) <=2 and  min((N-abs(k-c1)),abs(k-c1)) <=2:
                flag=True 
            elif min((N-abs(i-a2)),abs(i-a2)) <=2 and  min((N-abs(j-b2)),abs(j-b2)) <=2 and  min((N-abs(k-c2)),abs(k-c2)) <=2:
                flag=True 
            
            if flag==True :
                cnt+=1

print(cnt)
