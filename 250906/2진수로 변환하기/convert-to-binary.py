n = int(input())

# Please write your code here.
arr=[]

while True:
    if n<2:
        arr.append(n)
        break
    arr.append(n%2) #나머지 
    n//=2 #2로 나눈 몫 

results=arr[::-1]
for i in results:
    print(i,end="")