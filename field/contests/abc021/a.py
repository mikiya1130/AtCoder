N = int(input())

div, mod = divmod(N, 2)

print(div + mod)
for _ in range(div):
    print(2)
if mod == 1:
    print(1)
