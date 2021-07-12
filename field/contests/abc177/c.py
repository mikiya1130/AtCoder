import itertools

N = int(input())
A = list(map(int, input().split()))
A_acc = list(itertools.accumulate(A))

sum = 0
for i, j in zip(A[1:], A_acc[:-1]):
    sum += i * j

print(sum % (10 ** 9 + 7))
