n = int(input())
numbers = list(map(int, input().split()))

max_num = numbers[0] 
for x in numbers:
    if x > max_num:
        max_num = x

print(max_num)
