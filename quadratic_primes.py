"""Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| < 1000
Find the product of the coefficients, a and b,
for the quadratic expression that produces
the maximum number of primes for
consecutive values of n,
starting with n = 0."""

from timeit import default_timer as timer
import math
from primes import *


def longest_prime_quadratic(a_lim, b_lim):
    longest = {
        "count": 0,
        "a": None,
        "b": None
    }
    primes = set(primes_upto(50000))
    for a in range((1 - a_lim), a_lim):
        for b in range(2, b_lim):  # case n = 0: b must be prime
            if b in primes:
                n = 0
                while (n**2 + a*n + b) in primes:
                    n += 1
                if n > longest["count"]:
                    longest["count"] = n
                    longest["a"], longest["b"] = a, b
    return longest["a"] * longest["b"]

start = timer()
ans = longest_prime_quadratic(1000, 1000)
elapsed_time = (timer() - start) * 1000  # s --> ms

print("\nFound %d in %r ms.\n" % (ans, elapsed_time))
