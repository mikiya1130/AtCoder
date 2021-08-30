import itertools

N = int(input())
ST = [input().split() for _ in range(N)]

for st1, st2 in itertools.combinations(ST, 2):
    if st1 == st2:
        print("Yes")
        break
else:
    print("No")
