N = int(input())

sum = 0
for _ in range(N):
    A, B = map(int, input().split())

    sum += (B - A + 1) * (A + B) // 2

print(sum)
