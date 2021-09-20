import bisect

N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
time = 0
while True:
    try:
        time = A[bisect.bisect_left(A, time)]
        time += X
        time = B[bisect.bisect_left(B, time)]
        time += Y
        ans += 1
    except IndexError:
        break

print(ans)
