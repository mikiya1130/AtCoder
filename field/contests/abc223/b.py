S = input()
N = len(S)

first = "z" * 1000
last = "a"
for _ in range(N):
    if S < first:
        first = S
    if S > last:
        last = S
    S = S[1:] + S[0]

print(first)
print(last)
