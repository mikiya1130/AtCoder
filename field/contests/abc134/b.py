import math

N, D = map(int, input().split())
Range = 2 * D + 1
print(math.ceil(N / Range))
