N, K = map(int, input().split())
S = input()

L = []
lenL = 0

n = 1
for i in range(1, N):
    if S[i - 1] == S[i]:
        n += 1
    else:
        L.append(n)
        lenL += 1
        n = 1
L.append(n)
lenL += 1
if S[0] == "0":
    L = [0] + L
    lenL += 1
if S[-1] == "0":
    L = L + [0]
    lenL += 1

width = 2 * K + 1
if width >= lenL:
    print(sum(L))
else:
    s = sum(L[:width])
    ans = s
    for i in range(width, lenL, 2):
        s = s + (L[i] + L[i + 1]) - (L[i - width] + L[i - width + 1])
        ans = max(ans, s)

    print(ans)
