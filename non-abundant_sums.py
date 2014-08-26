from math import sqrt
from itertools import combinations
from timeit import default_timer as timer
from bisect import bisect_left


def abundants_upto(n):
    divisor_sums = [0] * (n + 1)
    for divisor in range(2, n + 1):
        for index in range(divisor, n + 1, divisor):
            divisor_sums[index] += divisor
    return [index for index, x in enumerate(divisor_sums) if x > 2 * index]


def summable_abundants(n):
    # finds all numbers below a number which can be expressed
    # as the sum of two abundant numbers
    abundants = abundants_upto(n)
    abundant_sums = set()
    stop = bisect_left(abundants, abundants[-1]//2)
    for index, abundant in enumerate(abundants[:stop]):
        max_addend = n - abundant
        for addend in abundants[index:]:
            if addend > max_addend:
                break
            abundant_sums.add(abundant + addend)
    return abundant_sums

start = timer()
ans = (28123 * 28124 / 2) - sum(summable_abundants(28123))
elapsed_time = (timer() - start) * 1000
print("\nFound %d as the sum in %d ms.\n" % (ans, elapsed_time))
