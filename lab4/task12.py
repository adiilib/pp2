import json

def deep_diff(a, b, path=""):
    diffs = []

    keys = set(a.keys()) | set(b.keys())

    for k in keys:
        new_path = f"{path}.{k}" if path else k

        if k not in a:
            diffs.append((new_path, "<missing>", b[k]))
        elif k not in b:
            diffs.append((new_path, a[k], "<missing>"))
        else:
            if isinstance(a[k], dict) and isinstance(b[k], dict):
                diffs.extend(deep_diff(a[k], b[k], new_path))
            elif a[k] != b[k]:
                diffs.append((new_path, a[k], b[k]))

    return diffs


obj1 = json.loads(input())
obj2 = json.loads(input())

differences = deep_diff(obj1, obj2)

if not differences:
    print("No differences")
else:
    for path, old, new in sorted(differences):
        old_val = old if old == "<missing>" else json.dumps(old, separators=(',', ':'))
        new_val = new if new == "<missing>" else json.dumps(new, separators=(',', ':'))
        print(f"{path} : {old_val} -> {new_val}")