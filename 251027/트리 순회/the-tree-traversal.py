n = int(input())

left = [0] * 26
right = [0] * 26

for _ in range(n):
    x, l, r = input().split()
    left[ord(x) - ord("A")] = l
    right[ord(x) - ord("A")] = r

arr=[None]*(n+1)

def preorder(n):
    if n=='.':
        return 
    print(n,end="")
    preorder(left[ord(n)-ord("A")])
    preorder(right[ord(n)-ord("A")])
def inorder(n):
    if n=='.':
        return 
    inorder(left[ord(n)-ord("A")])
    print(n,end="")
    inorder(right[ord(n)-ord("A")])

def postorder(n):
    if n=='.':
        return 
    postorder(left[ord(n)-ord("A")])
    postorder(right[ord(n)-ord("A")])
    print(n,end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")