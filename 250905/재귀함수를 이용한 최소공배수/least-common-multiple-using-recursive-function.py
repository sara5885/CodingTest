n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def find_gcd(a,b):
    while b!=0:
        a,b=b,a%b 
    return a
def compute_abs(a,b):
    global arr 
    return arr[a]*arr[b]/find_gcd(arr[a],arr[b])

tmp=0
def find_abs(tmp_abs,i):
    global arr 
    global tmp 
    #print(f"find_abs({tmp_abs,i})")
    if i==-1:
        return int(tmp) 
    
    tmp=arr[i]*tmp_abs/find_gcd(arr[i],tmp_abs)
    return find_abs(tmp,i-1)



# current_abs, idx 
print(find_abs(1,n-1))    