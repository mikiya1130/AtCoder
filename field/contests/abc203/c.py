N, K = map(int, input().split())

village = {}
for i in range(N):
    A, B = map(int, input().split())
    if A in village:
        village[A] += B
    else:
        village[A] = B

village_key = sorted(village)

for k in village_key:
    if k <= K:
        K += village[k]
    else:
        break

print(K)
