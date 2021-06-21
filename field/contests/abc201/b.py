N = int(input())

dict = {}
for _ in range(N):
    S, T = input().split()
    dict[int(T)] = S

key_desc = sorted(dict.keys(), reverse=True)
print(dict[key_desc[1]])
