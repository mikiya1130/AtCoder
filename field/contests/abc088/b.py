N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

print(sum(A[::2]) - sum(A[1::2]))
