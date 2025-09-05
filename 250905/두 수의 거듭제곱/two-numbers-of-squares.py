a, b = map(int, input().split())


def compute_power(a,b):
    answer=1
    while b!=0:
        answer*=a 
        b-=1 
    return answer

print(compute_power(a,b))