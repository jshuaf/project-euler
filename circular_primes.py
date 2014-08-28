from primes import test as is_prime
from itertools import product
from timeit import default_timer as timer


def is_circular(digits):
        digits = list(digits)
        for digit in digits:
            if not is_prime(int(''.join(map(str, digits)))):
                return False
            else:
                digits.append(digits.pop(0))
        return True


def find_circular_primes_under(limit):
    if type(limit) != int or limit <= 2:
        return "Error: primes are positive integers greater than 1."
    elif limit <= 11:
        sum = 0
        for k in range(limit):
            if is_prime(k):
                sum += 1
        return sum
    else:
        sum = 4
        for k in range(2, len(str(limit))):
            for combo in product([1, 3, 7, 9], repeat=k):
                if is_circular(combo):
                    sum += 1
        return sum

start = timer()
ans = find_circular_primes_under(10**6)
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
