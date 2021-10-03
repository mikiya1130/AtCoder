S = input()
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

for l, r in LR:
    S = S[: l - 1] + "".join(reversed(list(S[l - 1 : r]))) + S[r:]

print(S)
