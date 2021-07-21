import collections

H, W, K = map(int, input().split())

C = []
n_col = []
n_row = []
n_all = None

for h in range(H):
    c = input()
    n_row.append(collections.Counter(c)["#"])
    C.append(c)

for w in range(W):
    n_col.append(collections.Counter([c[w] for c in C])["#"])

n_all = sum(n_row)

ans = 0
for h in range(2 ** H):
    for w in range(2 ** W):
        sum = 0
        select_row = []
        select_col = []

        for n_h in range(H):
            if h & 1 << n_h:
                sum += n_row[n_h]
                select_row.append(n_h)

        for n_w in range(W):
            if w & 1 << n_w:
                sum += n_col[n_w]
                select_col.append(n_w)

        for i in select_row:
            for j in select_col:
                if C[i][j] == "#":
                    sum -= 1

        if n_all - sum == K:
            ans += 1

print(ans)
