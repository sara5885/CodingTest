#250913 (23:26)
N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

bomb_arr=[]

for i in range(N):
    for j in range(i+1,N):
        if num[i]==num[j] and abs(i-j)<=K:
            bomb_arr.append(num[i])

bomb_arr.sort()
if len(bomb_arr)==0:
    print(-1)
else:
    print(bomb_arr[-1])