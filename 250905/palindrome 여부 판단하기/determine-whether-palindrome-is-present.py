A = input()


def check_palindrome(A):
    return A[::-1]

B=check_palindrome(A)

if A==B:
    print('Yes')
else:
    print('No')