"""
Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""

import itertools
def generate_primes(n):
    prime = [True for _ in range(n + 1)]
    prime[0], prime[1] = False, False
    for i in range(int(n**0.5) + 1):
        if prime[i]:
            for j in range(i + i, n + 1, i):
                prime[j] = False
    return (i for i in range(2, n + 1) if prime[i])

# N = 10
print(generate_primes(10))