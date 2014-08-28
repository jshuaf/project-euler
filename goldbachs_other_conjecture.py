from primes import primes_upto, test as is_prime
from itertools import count
from timeit import default_timer as timer


def goldbach_other_conject(n):  # if an odd composite is prime + 2 * square
    for k in primes:
        if k > n:
            return False
        elif (((n - k)/2)**0.5).is_integer():
            return True
    return False

primes = primes_upto(500000)
checking_primes = set(primes)
start = timer()
for x in range(9, 500000, 2):
    if x not in checking_primes and not goldbach_other_conject(x):
        ans = x
        break

elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
