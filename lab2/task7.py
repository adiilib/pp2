n = int(input())
numbers = list(map(int, input().split()))

max_num = numbers[0]   
pos = 1                 

for i in range(1, n):
    if numbers[i] > max_num:
        max_num = numbers[i]
        pos = i + 1     

print(pos)
