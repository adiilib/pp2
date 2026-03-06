n = int(input())
nums = map(int, input().split())

count = sum(map(bool, nums))

print(count)