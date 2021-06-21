import statistics

A = list(map(int, input().split()))

median = statistics.median(A)
mean = statistics.mean(A)

if median == mean:
    print('Yes')
else:
    print('No')
