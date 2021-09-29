import itertools

N = int(input())

for ans in itertools.product("abc", repeat=N):
    print(*ans, sep="")
