import json
import re

data = json.loads(input())
q = int(input())

for _ in range(q):
    query = input()
    cur = data
    ok = True

    
    parts = re.findall(r'[^[.\]]+|\[\d+\]', query)

    for part in parts:
        if part.startswith('['):
            idx = int(part[1:-1])
            if isinstance(cur, list) and 0 <= idx < len(cur):
                cur = cur[idx]
            else:
                ok = False
                break
        else:
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                ok = False
                break

    if ok:
        print(json.dumps(cur, separators=(',', ':')))
    else:
        print("NOT_FOUND")