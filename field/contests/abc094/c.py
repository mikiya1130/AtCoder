N = int(input())
X = list(map(int, input().split()))

center = N // 2
sortX = sorted(X)
l = sortX[center - 1]
r = sortX[center]

for x in X:
    if x > l:
        print(l)
    else:
        print(r)
