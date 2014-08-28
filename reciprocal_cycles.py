"""Find the value of d < 1000 for which
1/d contains the longest recurring cycle
in its decimal fraction part."""

from timeit import default_timer as timer
import math
from decimal import *
from fractions import gcd
from functools import reduce
from primes import factorization


def period_if_prime(k):
    period = 1
    while (10**period - 1) % k != 0:
        period += 1
    return period  # returns period of 1/d if d is prime


def lcm(numbers):  # finds lcm of list of #s
    return reduce(lambda a, b: (a * b) / gcd(a, b), numbers)


def longest_period(n):
    longest = [0, 0]  # length, num
    for x in range(3, n):  # check all up to d for 1/d
        pf = factorization(x)
        if all(p == 2 or p == 5 for p in pf):  # doesn't repeat
            continue
        elif len(pf) == 1:  # run prime function
            if longest[0] < period_if_prime(x):
                longest = [period_if_prime(x), x]
        else:
            fact = pf
            periods = []
            for k in fact:
                if k != 2 and k != 5:
                    if fact.count(k) == 1:
                        periods.append(period_if_prime(k))
                    else:
                        temp = k**(fact.count(k) - 1)
                        periods.append((period_if_prime(k)) * temp)
            if lcm(periods) > longest[0]:
                longest = [lcm(periods), x]
    return longest[1]

start = timer()
ans = longest_period(1000)
elapsed_time = (timer() - start) * 1000  # seconds --> milliseconds
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
