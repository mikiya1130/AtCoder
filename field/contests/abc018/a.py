ABC = [int(input()) for _ in range(3)]
sABC = sorted(ABC, reverse=True)
for n in ABC:
    print(sABC.index(n) + 1)
