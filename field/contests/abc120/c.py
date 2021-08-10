S = input()

zero = 0
one = 0

for s in S:
    if s == '0':
        zero += 1
    elif s == '1':
        one += 1

print(min(zero, one) * 2)
