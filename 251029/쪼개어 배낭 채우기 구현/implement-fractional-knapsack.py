# 251029 (17:19)
n, m = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(n)])
w, v = list(w), list(v)

arr=[]
for i in range(n):
    arr.append([v[i]/w[i],i])

arr.sort(key=lambda x: -x[0])
# arr 순서대로 담아주기 : 
j_idx=0
value=0
while m>0:
    if not 0<=j_idx<n:
        break
    j_num=arr[j_idx][1]
    j_price=v[j_num]
    j_weight=w[j_num]
    if m>j_weight: #모두 담을 수 있는 것 
        m-=j_weight
        value+=j_price
    else: # 쪼개서 담기 
        value+=m*arr[j_idx][0]
        m=0
    j_idx+=1 

print(f"{value:.3f}")

