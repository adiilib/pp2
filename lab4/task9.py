def powers_of_two(n):
    for i in range(n + 1):
        yield 2 ** i

n = int(input())

first = True
for p in powers_of_two(n):
    if not first:
        print(' ', end='')
    print(p, end='')
    first = False
print()