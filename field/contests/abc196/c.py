N = input()

l = len(N)
if l % 2 == 1:
    N = '9' * (l-1)
if l == 1:
    N = '00'

c = len(N) // 2
a = int(N[:-c])
b = int(N[-c:])

if a <= b:
    print(a)
else:
    print(a - 1)
