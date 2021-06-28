import collections

K = int(input())
S = list(input())[:4]
T = list(input())[:4]

S = dict(collections.Counter(S))
T = dict(collections.Counter(T))

S = {int(k): v for k, v in S.items()}
T = {int(k): v for k, v in T.items()}

card = [K] * 9

for k, v in S.items():
    card[k-1] -= v
for k, v in T.items():
    card[k-1] -= v

for i in range(1, 10):
    if i not in S:
        S[i] = 0
    if i not in T:
        T[i] = 0


def judge(SS, TT):
    sum_s = 0
    sum_t = 0

    for (s1, s2), (t1, t2) in zip(SS, TT):
        sum_s += s1 * 10 ** s2
        sum_t += t1 * 10 ** t2

    return sum_s > sum_t


win = 0
count = 0
for c1, n in enumerate(card, 1):
    for c2, m in enumerate(card, 1):
        if n == 0 or m == 0 or (c1 == c2 and n <= 1):
            continue

        if c1 == c2:
            m -= 1

        SS = S.copy()
        TT = T.copy()

        SS[c1] += 1
        TT[c2] += 1

        SS = sorted(SS.items(), key=lambda x: (x[1], x[0]), reverse=True)
        TT = sorted(TT.items(), key=lambda x: (x[1], x[0]), reverse=True)

        if judge(SS, TT):
            win += n * m
        count += n * m

print(win / count)
