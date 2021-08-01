N, A, B = map(int, input().split())

div, mod = divmod(N, (A + B))

if mod <= A:
    print(div * A + mod)
else:
    print(div * A + A)
