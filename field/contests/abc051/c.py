sx, sy, tx, ty = map(int, input().split())

print("U" * (ty - sy), end="")
print("R" * (tx - sx), end="")
print("D" * (ty - sy), end="")
print("L" * (tx - sx), end="")

print("L", end="")
print("U" * (ty - sy + 1), end="")
print("R" * (tx - sx + 1), end="")
print("D", end="")
print("R", end="")
print("D" * (ty - sy + 1), end="")
print("L" * (tx - sx + 1), end="")
print("U", end="")

print()
