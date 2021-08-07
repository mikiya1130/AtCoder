S = input()

ng = ""
for s in S:
    if ng == "L":
        ng = "R"
    else:
        ng = "L"

    if s == ng:
        print("No")
        break
else:
    print("Yes")
