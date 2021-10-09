N = int(input())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


A = 2025 - N
A = make_divisors(A)
l = len(A)

for i in range(l):
    if A[i] <= 9 and A[l - i - 1] <= 9:
        print(A[i], "x", A[l - i - 1])
