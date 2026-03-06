n = int(input())
nums = map(int, input().split())

result = sorted(set(nums))

print(*result)