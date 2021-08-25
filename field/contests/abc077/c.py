import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()

ans = 0
for b in B:
    ans += bisect.bisect_left(A, b) * (N - bisect.bisect_right(C, b))

print(ans)
