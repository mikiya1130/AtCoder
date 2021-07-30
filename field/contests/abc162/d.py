import itertools

N = int(input())
S = input()

R, G, B = set(), set(), set()
countR, countG, countB = 0, 0, 0
for i in range(N):
    if S[i] == "R":
        R.add(i)
        countR += 1
    elif S[i] == "G":
        G.add(i)
        countG += 1
    elif S[i] == "B":
        B.add(i)
        countB += 1

if countR >= countG and countR >= countB:
    R, B = B, R
    countB = countR
elif countG >= countR and countG >= countB:
    G, B = B, G
    countB = countG

ans = 0
for li1, li2 in itertools.product(R, G):
    if li1 > li2:
        li1, li2 = li2, li1
    diff = li2 - li1
    li3 = {li1 - diff, li2 + diff}
    if diff % 2 == 0:
        li3.add(li1 + diff // 2)

    count = 0
    for l in li3:
        if l in B:
            count += 1
    ans += countB - count

print(ans)
