import itertools

X = int(input())

for x, y in itertools.product(range(-200, 201), repeat=2):
    if x ** 5 - y ** 5 == X:
        print(x, y)
        break
