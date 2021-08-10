A = [int(input()) for _ in range(5)]

B = [] * 5
C = [] * 5
for a in A:
    div, mod = divmod(a, 10)
    if mod != 0:
        C.append(mod)
        div += 1
    B.append(div)

if not C:
    C = [10]
print(sum(B)*10-10+min(C))
