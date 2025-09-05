n, m = map(int, input().split())

# euclidean algorithm

def find_gcd(n,m):
    while m!=0:
        n,m=m,n%m
    return n 

a=max(n,m)
b=min(n,m)
gcd=find_gcd(a,b)
print(int(a*b/gcd))

    