ABCD = [int(n) for n in list(input())]

for i in range(2 ** 3):
    calc = ABCD[0]
    ans = str(ABCD[0])

    for j, n in enumerate(ABCD[1:]):
        if i >> j & 1:
            calc += n
            ans += "+" + str(n)
        else:
            calc -= n
            ans += "-" + str(n)

    if calc == 7:
        print(ans + "=7")
        break
