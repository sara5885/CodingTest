str = input()

# Please write your code here.
stack_arr=[]
right_flag=True
for i in range(len(str)):
    if str[i]=='(':
        stack_arr.append(str[i])
    elif str[i]==')':
        if len(stack_arr)==0 or stack_arr[-1]==')':
            right_flag=False 
            break 
        else:
            del stack_arr[-1]

if len(stack_arr)!=0:
    right_flag=False 

if right_flag==True :
    print('Yes')
else:
    print('No')