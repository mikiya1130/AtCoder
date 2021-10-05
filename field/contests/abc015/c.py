import itertools

N, K = list(map(int, input().split()))
T = [list(map(int, input().split())) for _ in range(N)]

for Q in itertools.product(range(K), repeat=N):
    xor = 0
    for n, q in enumerate(Q):
        xor ^= T[n][q]
    if xor == 0:
        print("Found")
        break
else:
    print("Nothing")
