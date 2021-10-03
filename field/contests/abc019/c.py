import collections

N = int(input())
A = list(map(int, input().split()))


def div2(a):
    while a % 2 == 0:
        a //= 2
    return a


Ax2 = [div2(a) for a in A]
Ax2 = collections.Counter(Ax2)

print(len(Ax2))
