N, B = map(int, input().split())
result=[]
while True:
    if N<B:
        result.append(N)
        break
    result.append(N%B)
    N=N//B

result=result[::-1]
for i in result:
    print(i,end="")