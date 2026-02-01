n, l, r = map(int, input().split())
arr = list(map(int, input().split()))

l_index = l - 1
r_index = r - 1

arr[l_index:r_index+1] = arr[l_index:r_index+1][::-1]

print(*arr)
