n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.

while True:
    stack=[] # [값, 연속개수]
    exploded=False 
    for num in numbers:
        if stack and stack[-1][0]==num:
            stack[-1][1]+=1 #가장 위에있는 벽돌의 개수 하나 증가 
        else:
            # 새로운 벽돌 추가 
            stack.append([num,1])
        
        # if stack[-1][1]>=m:
        #     stack.pop()
        #     exploded=True 
    # stack => numbers 
    # print(stack)
    # temp=[]
    # for num,cnt in stack:
    #     temp.extend([num]*cnt)
    # numbers=temp 
    # print(numbers)
    temp=[]
    for num, cnt in stack:
        if cnt < m :
            temp.extend([num]*cnt)
        else:
            exploded=True 
    numbers=temp
    # print(numbers)
    if not exploded : break 

print(len(numbers))
for num in numbers:
    print(num)