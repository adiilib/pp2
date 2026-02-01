n = int(input())
numbers = [input().strip() for _ in range(n)]

freq = {} 
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

count = sum(1 for val in freq.values() if val == 3)

print(count)
