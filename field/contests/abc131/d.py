N = int(input())

Task = []
for _ in range(N):
    A, B = map(int, input().split())
    Task.append((A, B))

Task = sorted(Task, key=lambda t: t[1])

time = 0
for a, b in Task:
    time += a
    if time > b:
        print("No")
        break
else:
    print("Yes")
