N = input()

ans = 0
l = len(N)
for i in range(2 ** l):
    A, B = [], []
    for j in range(l):
        if i >> j & 1:
            A.append(N[j])
        else:
            B.append(N[j])

    if len(A) == 0 or len(B) == 0:
        continue

    if set(A) == {"0"} or set(B) == {"0"}:
        continue

    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)

    A = int("".join(A))
    B = int("".join(B))

    ans = max(A * B, ans)

print(ans)
