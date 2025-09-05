a, o, c = input().split()
a = int(a)
c = int(c)

def summ(a,b):
    return a+b
def diff(a,b):
    return a-b
def mult(a,b):
    return a*b
def mode(a,b):
    return a//b 


def compute(a,o,c):
    if o=='+':
        print(f"{a} + {c} = {summ(a,c)}")
    elif o=='-':
        print(f"{a} - {c} = {diff(a,c)}")
    elif o=='/':
        print(f"{a} / {c} = {mode(a,c)}")
    elif o=='*':
        print(f"{a} * {c} = {mult(a,c)}")
    else:
        print('False')

compute(a,o,c)