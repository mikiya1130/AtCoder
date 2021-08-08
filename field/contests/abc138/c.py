N = int(input())
V = list(map(int, input().split()))

V = sorted(V)

mean = V[0]
for v in V[1:]:
    mean = (mean + v) / 2

print(mean)
