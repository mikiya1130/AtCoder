N = int(input())
S = input()

stack = 0
left = 0
for s in S:
    if s == "(":
        if stack < 0:
            left += -stack
            stack = 0
        stack += 1
    elif s == ")":
        stack -= 1

if stack < 0:
    left += -stack
    stack = 0


print("(" * left + S + ")" * stack)
