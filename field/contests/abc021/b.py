N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

P += [a, b]
if len(set(P)) == K + 2:
    print("YES")
else:
    print("NO")
