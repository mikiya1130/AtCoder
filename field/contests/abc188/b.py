_ = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0
for a, b in zip(A, B):
    sum += a * b

if sum == 0:
    print('Yes')
else:
    print('No')
