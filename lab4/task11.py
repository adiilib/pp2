import json

def patch_obj(s, p):
    for k in p:
        if p[k] is None:
            s.pop(k, None)
        elif isinstance(p[k], dict) and isinstance(s.get(k), dict):
            patch_obj(s[k], p[k])
        else:
            s[k] = p[k]
    return s

s = json.loads(input())
p = json.loads(input())

print(json.dumps(patch_obj(s, p), sort_keys=True, separators=(',', ':')))