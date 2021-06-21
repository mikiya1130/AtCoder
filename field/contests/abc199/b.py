N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxA = max(A)
minB = min(B)

print(max(minB - maxA + 1, 0))
