n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dot = 0

for x,y in zip(a,b):
    dot += x*y

print(dot)

