from primes import primes_upto
from primes import test as is_prime
from timeit import default_timer as timer


def follows_property(n):
    n1 = n + 3330
    n2 = n1 + 3330
    if is_prime(n1) and is_prime(n2):
        digits_n = [int(x) for x in str(n)]
        digits_n1 = [int(x) for x in str(n1)]
        digits_n2 = [int(x) for x in str(n2)]
        if sorted(str(n)) == sorted(str(n1)) == sorted(str(n2)):
            return [n, n1, n2]
    else:
        return False


start = timer()
four_digit_primes = [x for x in primes_upto(10000) if len(str(x)) == 4]
for prime in four_digit_primes:
    property_true = follows_property(prime)
    if property_true and prime != 1487:
        ans = ''
        for string in map(str, property_true):
            ans += string
        break

elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %s in %d ms.\n" % (ans, elapsed_time))
