n = int(input())

# Please write your code here.
def solve(current_len):
    if current_len==n:
        return 1 
    elif current_len>n:
        return 0 
    
    count =0
    count += solve(current_len+1)
    count+=solve(current_len+2)
    count+=solve(current_len+3)
    count+=solve(current_len+4)

    return count 

print(solve(0))