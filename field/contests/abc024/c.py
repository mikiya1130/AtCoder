N, D, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(D)]
ST = [list(map(int, input().split())) for _ in range(K)]

for s, t in ST:
    pos = s
    goRight = s < t
    for j, (l, r) in enumerate(LR):
        if l <= pos <= r:
            if goRight:
                pos = min(r, t)
            else:
                pos = max(l, t)

            if pos == t:
                print(j + 1)
                break
