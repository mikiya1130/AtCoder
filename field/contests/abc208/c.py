N, K = map(int, input().split())
a = list(map(int, input().split()))

n = K // N
m = K % N

b = sorted(a)[m]

for aa in a:
    if aa < b:
        print(n+1)
    else:
        print(n)
