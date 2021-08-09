N = int(input())
SP = []
for i in range(1, N + 1):
    S, P = input().split()
    SP.append((i, S, int(P)))

SP = sorted(SP, key=lambda x: x[2], reverse=True)
SP = sorted(SP, key=lambda x: x[1])

for sp in SP:
    print(sp[0])
