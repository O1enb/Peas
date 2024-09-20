numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for num in numbers:
    is_prime = True
    if num == 1:
        continue
    for x in range(2,num-1):
        if num % x == 0:
            not_primes.append(num)
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print('Primes:', primes)
print('Not primes:', not_primes)