n = int(input())

def print_one_rect(n):
    i=1
    for _ in range(n):
        for _ in range(n):
            if i%10==0:
                i+=1
            print(i%10,end=" ")
            i+=1
        print('')

print_one_rect(n)