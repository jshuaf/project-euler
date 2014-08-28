from itertools import permutations
from primes import test as is_prime
from timeit import default_timer as timer


start = timer()
for k in range(7, 1, -1):  # can't be 9-digit b/c sum of digits is 45
    greatest = 0
    for combo in list(permutations(range(1, k + 1), k)):
        number = int(''.join(map(str, list(combo))))
        if number > greatest and is_prime(number):
            greatest = number
    if greatest:
        break

ans = greatest
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
