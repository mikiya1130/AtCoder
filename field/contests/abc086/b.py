x = input()

x = x.replace(" ", "")
x = int(x)
for i in range(318):
    if i * i == x:
        print("Yes")
        break
else:
    print("No")
