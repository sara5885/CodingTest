N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# 가격/무게 : 가성비 좋은 
arr=[]
for i in range(N):
    arr.append((i, v[i]/w[i]))
arr.sort(key=lambda x:-x[1])
# num, weight = arr[idx]
# v[w] : 무게, 
# print(arr)
ans=0
idx=0
while M>0:
    num,weight=arr[idx]
    if M>=w[num]: #하나 다 하기 
        ans+=v[num]
        M-=w[num]
    else: # 쪼개서 넣기 
        # 3남았는데 최대 무게가 4면 여기서 3만 넣기  (3/4)
        ans+=v[num]*M/w[num]
        M=0
    if idx+1<N :
        idx+=1 
# print(round(ans,3))
print(f"{ans:.3f}")

# 무게는 최대 M이 최대 M>0
# 가격/무게 제일 좋은 순서대로 하는데
    # 이 때 최대 무게 만큼 담을 수 있음 (보석이 하나씩만있음)
