A, B, C = map(int, input().split())

M = max(A, B, C)
S = (M - A) + (M - B) + (M - C)
if S % 2 == 0:
    print(S // 2)
else:
    print(S // 2 + 2)
