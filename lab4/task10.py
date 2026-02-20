def limited_cycle(lst, n):
    for _ in range(n):
        for item in lst:
            yield item

lst = input().split()
n = int(input())

first = True
for item in limited_cycle(lst, n):
    if not first:
        print(' ', end='')
    print(item, end='')
    first = False
print()