numb = [i for i in range(1, 16, 1)]
print(numb)

primes = []
not_primes = []
is_prime = True

for i in numb:
    for j in range(2, i, 1):
        if i%j == 0:
            is_prime = False
            not_primes.append(i)
            break

    if (is_prime == True) and (i != 1):
        primes.append(i)

    is_prime = True

print('Список простых чисел: ', primes)
print('Список непростых чисел: ', not_primes)