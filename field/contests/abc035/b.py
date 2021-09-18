import collections

S = input()
T = int(input())

cnt = collections.Counter(S)

ans = abs(cnt["L"] - cnt["R"]) + abs(cnt["U"] - cnt["D"])
if T == 1:
    ans += cnt["?"]
else:
    if ans >= cnt["?"]:
        ans -= cnt["?"]
    else:
        ans = (cnt["?"] - ans) % 2

print(ans)
