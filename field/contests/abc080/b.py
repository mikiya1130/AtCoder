N = int(input())
i = sum([int(n) for n in list(str(N))])
if N % i == 0:
    print("Yes")
else:
    print("No")
