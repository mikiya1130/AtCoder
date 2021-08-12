N = int(input())
W = [input() for _ in range(N)]

tail = W[0][0]
used = set()

for w in W:
    if w[0] != tail or w in used:
        print("No")
        break

    tail = w[-1]
    used.add(w)
else:
    print("Yes")
