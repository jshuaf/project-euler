import math


def sum_of_divisors(n):
    total = 0
    for x in range(1, math.trunc(math.sqrt(n)) + 1):
        if n % x == 0:
            total += x
            if math.sqrt(n) != x and x != 1:
                total += n/x
    return total


def amicable_nums_under(limit):
    divisor_sums = {}
    for x in range(2, limit):
        divisor_sums[x] = sum_of_divisors(x)
    amicables = []
    for key in divisor_sums:
        if divisor_sums[key] != 1:
            if divisor_sums[key] <= len(divisor_sums):
                if divisor_sums[key] != key:
                	if divisor_sums[divisor_sums[key]] == key:
                        amicables.append(key)

    return amicables

print("\nFound %d numbers.\n" % sum(amicable_nums_under(10000)))
