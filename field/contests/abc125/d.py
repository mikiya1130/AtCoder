N = int(input())
A = list(map(int, input().split()))

zero = False
minus = 0
minimum = 10 ** 9
for i in range(N):
    if A[i] == 0:
        zero = True
    elif A[i] < 0:
        minus += 1
        A[i] *= -1
    minimum = min(minimum, A[i])

if zero or minus % 2 == 0:
    print(sum(A))
else:
    print(sum(A) - 2 * minimum)
