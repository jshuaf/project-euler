from timeit import default_timer as timer


def product(n):
    from functools import reduce  # Valid in Python 2.6+, required in Python 3
    from operator import mul
    return reduce(mul, n, 1)


def find_champernowne_index(d):
    constant = ""
    for k in range(1, d + 1):
        constant += str(k)
        if len(constant) >= d:
            return int(constant[d-1])

start = timer()
ans = product(find_champernowne_index(10**x) for x in range(0, 7))
elapsed_time = (timer() - start) * 1000  # s --> ms

print("Found %d in %d ms." % (ans, elapsed_time))
