N = int(input())

T = [0] * 289
for _ in range(N):
    s, e = map(int, input().split("-"))
    T[12 * (s // 100) + (s % 100 - (s % 100) % 5) // 5] += 1
    T[12 * (e // 100) + (e % 100 + 4 - (e % 100 + 4) % 5) // 5] -= 1

tmp_i = -1
t = 0
for i in range(289):
    t += T[i]
    if tmp_i == -1 and t >= 1:
        tmp_i = i
    elif tmp_i != -1 and t <= 0:
        print(
            "{:02d}{:02d}-{:02d}{:02d}".format(
                tmp_i // 12, (tmp_i % 12) * 5, i // 12, (i % 12) * 5
            )
        )
        tmp_i = -1
