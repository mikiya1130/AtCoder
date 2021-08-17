A, B, K = map(int, input().split())

half = (B - A + 1) // 2
if K <= half:
    ans = list(range(A, A + K)) + list(range(B - K + 1, B + 1))
else:
    ans = list(range(A, B + 1))

for a in ans:
    print(a)
