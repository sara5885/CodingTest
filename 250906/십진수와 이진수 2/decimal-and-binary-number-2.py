N = input()
num_10=0
# Please write your code here.
for i in range(len(N)):
    num_10=num_10*2+int(N[i])

num_10*=17
result=[]
while True:
    if num_10<2:
        result.append(num_10)
        break
    result.append(num_10%2)
    num_10=num_10//2

result=result[::-1]
for i in result:
    print(i,end="")