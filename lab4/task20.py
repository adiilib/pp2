g = 0
n = 0

for _ in range(int(input())):
    scope, val = input().split()
    val = int(val)
    if scope == "global":
        g += val
    elif scope == "nonlocal":
        n += val

print(g, n)