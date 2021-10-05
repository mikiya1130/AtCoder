N = int(input())
A = list(map(int, input().split()))

A = [a for a in A if a != 0]
s = sum(A)
n = len(A)

print((s + n - 1) // n)
