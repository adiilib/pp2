import importlib

for _ in range(int(input())):
    mod_path, attr = input().split()
    try:
        mod = importlib.import_module(mod_path)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    if not hasattr(mod, attr):
        print("ATTRIBUTE_NOT_FOUND")
    elif callable(getattr(mod, attr)):
        print("CALLABLE")
    else:
        print("VALUE")