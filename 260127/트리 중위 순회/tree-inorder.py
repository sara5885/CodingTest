# 260127 (16:17)
import math
K = int(input())
inorder_traversal = list(map(int, input().split()))

center=len(inorder_traversal)//2
start=0
end=len(inorder_traversal)
depth=0
depth_max=2**depth
depth_cnt=0
tree=[[] for _ in range(K)] # depth 개수만큼 2차원 list 
# print(tree)

def inorder(arr,depth):
    # depth update 조건에 부합하면 depth+=1 , 해당 depth의 노드 개수 : 2**depth 
    if not arr :
        return 
    center=len(arr)//2
    tree[depth].append(arr[center])
    inorder(arr[:center],depth+1)
    inorder(arr[center+1:], depth+1)
inorder(inorder_traversal, 0)

for row in tree:
    for col in row:
        print(col, end=" ")
    print()