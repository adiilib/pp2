n = int(input())
nums = map(int, input().split())

print("Yes" if all(x >= 0 for x in nums) else "No")