n = int(input())
doc = {}
output = []

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "set":
        key, value = cmd[1], cmd[2]
        doc[key] = value
    elif cmd[0] == "get":
        key = cmd[1]
        if key in doc:
            output.append(doc[key])
        else:
            output.append(f"KE: no key {key} found in the document")

print("\n".join(output))
