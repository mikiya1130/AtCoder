import collections

N = input()
N = collections.Counter(N)

sum = 0
for k, v in N.items():
    sum += int(k) * v

if sum % 9 == 0:
    print("Yes")
else:
    print("No")
