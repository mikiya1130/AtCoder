N = int(input())


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    l = 0
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(len(str(i)))
            l += 1
            if i != n // i:
                upper_divisors.append(len(str(n // i)))
                l += 1
        i += 1
    return lower_divisors + upper_divisors[::-1], l


arr, l = make_divisors(N)

ans = 10 ** 10
for i in range(l):
    ans = min(ans, max(arr[i], arr[l - i - 1]))

print(ans)
