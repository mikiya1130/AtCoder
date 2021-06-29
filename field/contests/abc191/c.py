H, W = map(int, input().split())

S = []
for i in range(H):
    S.append(input())


def num_black(i, j):
    count = 0
    if S[i-1][j-1] == '#':
        count += 1
    if S[i-1][j] == '#':
        count += 1
    if S[i][j-1] == '#':
        count += 1
    if S[i][j] == '#':
        count += 1
    return count


ans = 0
for i in range(1, H):
    for j in range(1, W):
        n = num_black(i, j)
        if n == 1 or n == 3:
            ans += 1

print(ans)
