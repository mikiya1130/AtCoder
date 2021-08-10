import collections

S = input()

odd = collections.Counter(S[::2])
even = collections.Counter(S[1::2])
odd.setdefault("0", 0)
odd.setdefault("1", 0)
even.setdefault("0", 0)
even.setdefault("1", 0)

print(min(odd["0"] + even["1"], odd["1"] + even["0"]))
