n = int(input())
arr = list(map(int, input().split()))

freq = {}  
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

max_freq = max(freq.values())

most_frequent = min(key for key, val in freq.items() if val == max_freq)

print(most_frequent)
