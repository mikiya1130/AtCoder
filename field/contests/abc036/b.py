N = int(input())
S = [input() for _ in range(N)]

T = [[None] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        T[i][j] = S[N-j-1][i]

T = [''.join(t) for t in T]

print(*T, sep='\n')
