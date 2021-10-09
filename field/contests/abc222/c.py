N, M = map(int, input().split())
A = [input() for i in range(2 * N)]

P = [[i, 0] for i in range(2 * N)]


def judge(h1, h2):
    if h1 == "G":
        if h2 == "G":
            return 0, 0
        elif h2 == "C":
            return 1, 0
        elif h2 == "P":
            return 0, 1
    elif h1 == "C":
        if h2 == "G":
            return 0, 1
        elif h2 == "C":
            return 0, 0
        elif h2 == "P":
            return 1, 0
    elif h1 == "P":
        if h2 == "G":
            return 1, 0
        elif h2 == "C":
            return 0, 1
        elif h2 == "P":
            return 0, 0


for i in range(M):
    for j in range(N):
        p1 = P[2 * j][0]
        p2 = P[2 * j + 1][0]

        h1 = A[p1][i]
        h2 = A[p2][i]

        s1, s2 = judge(h1, h2)

        P[2 * j][1] += s1
        P[2 * j + 1][1] += s2

    P.sort()
    P = sorted(P, key=lambda x: x[1], reverse=True)

for ans, _ in P:
    print(ans + 1)
