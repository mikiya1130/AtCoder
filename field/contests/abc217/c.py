N = int(input())
P = list(map(int, input().split()))

PQ = [(p, q) for q, p in enumerate(P, start=1)]
PQ = sorted(PQ)

for _, q in PQ:
    print(q, end=" ")
print()
