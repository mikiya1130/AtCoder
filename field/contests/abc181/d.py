import collections

S = list("{:03}".format(int(input())))
S = collections.Counter(S)

for i in range(10):
    if str(i) not in S:
        S[str(i)] = 0

mul8 = [i * 8 for i in range(1000 // 8)]

for m in mul8:
    if "0" in str(m):
        continue

    mul8_str = tuple("{:03}".format(m))
    for k, v in collections.Counter(mul8_str).items():
        if S[k] < v:
            break
    else:
        print("Yes")
        break
else:
    print("No")
