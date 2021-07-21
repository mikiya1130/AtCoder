N = int(input())

judge = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for i in range(N):
    S = input()
    judge[S] += 1

for k, v in judge.items():
    print("{} x {}".format(k, v))
