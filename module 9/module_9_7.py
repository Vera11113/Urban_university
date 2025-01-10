
def is_prime(func):

    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print('Составное')
                return n
            else: continue
        print('Простое')
        return n

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)
