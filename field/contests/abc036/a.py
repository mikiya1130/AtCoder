A, B = map(int, input().split())


def ceil(a, b):
    return (a + b - 1) // b


print(ceil(B, A))
