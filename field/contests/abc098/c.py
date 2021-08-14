N = int(input())
S = input()

W = [0] * N
E = [0] * N

cnt = 0
for i in range(N):
    W[i] = cnt
    if S[i] == "W":
        cnt += 1

cnt = 0
for i in range(N - 1, -1, -1):
    E[i] = cnt
    if S[i] == "E":
        cnt += 1

A = [w + e for w, e in zip(W, E)]
print(min(A))
