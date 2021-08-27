N = int(input())
A = list(map(int, input().split()))

B = {i: 0 for i in range(10 ** 5)}

for a in A:
    B[a] += 1

ans = 0
for i in range(10 ** 5 - 2):
    ans = max(ans, B[i] + B[i + 1] + B[i + 2])

print(ans)
