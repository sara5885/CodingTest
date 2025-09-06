a, b = map(int, input().split())
n = input()

# Please write your code here.
#1. n : A진수 -> 10 진수
#2. n : 10진수 -> B진수

num=0
for i in range(len(n)):
    num=num*a+int(n[i])

result=[]
while True:
    if num<b:
        result.append(num)
        break 
    result.append(num%b)
    num=num//b 

result=result[::-1]

for i in result:
    print(i,end="")