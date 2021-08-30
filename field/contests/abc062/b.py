H, W = map(int, input().split())
A = [input() for _ in range(H)]

for i in range(H):
    A[i] = "#" + A[i] + "#"

A = ["#" * (W + 2)] + A + ["#" * (W + 2)]

for a in A:
    print(a)
