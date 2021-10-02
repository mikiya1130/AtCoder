from collections import defaultdict

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

P = defaultdict(int)
for a, b in AB:
    P[a - 1] += 1
    P[a - 1 + b] -= 1

P = sorted(P.items(), key=lambda d: d[0])
Q = [0]
for _, p in P:
    Q.append(Q[-1] + p)
Q = Q[1:-1]

ans = defaultdict(int)
for i, q in enumerate(Q):
    ans[q] += P[i + 1][0] - P[i][0]

for i in range(N):
    print(ans[i + 1], end=" ")
print()
