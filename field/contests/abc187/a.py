A, B = input().split()

A, B = list(A), list(B)
A, B = [int(i) for i in A], [int(i) for i in B]
A, B = sum(A), sum(B)

if A >= B:
    print(A)
else:
    print(B)
