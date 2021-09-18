X = input()
N = int(input())
S = [input() for _ in range(N)]

S = sorted(S, key=lambda x: [X.index(xx) for xx in list(x)])

print(*S, sep="\n")
