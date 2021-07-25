counter = [
    0,  # c
    0,  # h
    0,  # o
    0,  # k
    0,  # u
    0,  # d
    0,  # a
    0,  # i
]

S = input()

for s in S:
    if s == "c":
        counter[0] += 1
        continue
    elif s == "h":
        counter[1] += counter[0]
    elif s == "o":
        counter[2] += counter[1]
    elif s == "k":
        counter[3] += counter[2]
    elif s == "u":
        counter[4] += counter[3]
    elif s == "d":
        counter[5] += counter[4]
    elif s == "a":
        counter[6] += counter[5]
    elif s == "i":
        counter[7] += counter[6]

print(counter[7] % (10 ** 9 + 7))
