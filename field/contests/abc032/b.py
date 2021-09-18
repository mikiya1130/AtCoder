s = input()
k = int(input())

l = len(s)

if l < k:
    print(0)
else:
    p = set()

    for i in range(l - k + 1):
        p.add(s[i : i + k])

    print(len(p))
