nums = list(map(int, input().split()))

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))

primes = list(filter(is_prime, nums))

print(*primes if primes else ["No primes"])
