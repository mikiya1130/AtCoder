import collections

w = input()

w = collections.Counter(w)

for v in w.values():
    if v % 2 == 1:
        print("No")
        break
else:
    print("Yes")
