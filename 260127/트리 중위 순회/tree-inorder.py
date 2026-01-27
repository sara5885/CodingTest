K = int(input())
n=(1<<K)-1 #(1<<K)는 2*i를 의미 
arr = [0]+list(map(int, input().split()))
tree=[0]*(n+1)
cnt=1
def inorder(num):
    global cnt 

    # num이 n보다 크면 빠져나가기
    if num>n: return 
    inorder(2*num)
    tree[num]=arr[cnt]
    cnt+=1
    inorder(2*num+1)

inorder(1)

for i in range(1,K+1): #depth만큼
    for j in range(1<<(i-1), 1<<i) : # 2**(i-1)부터 2**(i)까지 
        print(tree[j],end=" ")
    print()

