S = list(input())

dict = {'o': [], '?': [], 'x': []}
for i, s in enumerate(S):
    dict[s].append(i)

count = 0
for i in range(10000):
    n = []
    for _ in range(4):
        n.append(i % 10)
        i //= 10

    if set(n) >= set(dict['o']) and not(set(n) & set(dict['x'])):
        count += 1

print(count)
