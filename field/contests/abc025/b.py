N, A, B = map(int, input().split())
SD = [input().split() for _ in range(N)]

pos = 0
for s, d in SD:
    d = int(d)
    d = max(d, A)
    d = min(d, B)

    if s == "East":
        pos += d
    else:
        pos -= d

if pos > 0:
    print("East {}".format(pos))
elif pos < 0:
    print("West {}".format(-pos))
else:
    print(0)
