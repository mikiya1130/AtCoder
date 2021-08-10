import bisect

N, Q = map(int,input().split())
S = input()

AC = []
for i in range(1, N):
    if S[i] == 'C' and S[i-1] == 'A':
        AC.append(i)

for _ in range(Q):
    l, r = map(int,input().split())
    r -= 1

    idxl = bisect.bisect_left(AC, l)
    idxr = bisect.bisect_right(AC, r)
    print(idxr - idxl)
