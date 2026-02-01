n = int(input())
doc = {}

for _ in range(n):
    parts = input().split()
    command = parts[0]
    
    if command == "set":
        key = parts[1]
        value = parts[2]
        doc[key] = value
    elif command == "get":
        key = parts[1]
        if key in doc:
            print(doc[key])
        else:
            print(f"KE: no key {key} found in the document")
