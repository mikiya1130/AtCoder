N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

R = [set() for _ in range(N)]
for a, b in AB:
    R[a - 1].add(b - 1)
    R[b - 1].add(a - 1)

for i, r in enumerate(R):
    friends = set()
    for rr in r:
        friends |= R[rr]
    friends -= R[i]
    friends -= {i}
    print(len(friends))
