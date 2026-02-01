x = int(input())

if x <= 1:
    print("No")
else:
    is_prime = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    print("Yes" if is_prime else "No")
