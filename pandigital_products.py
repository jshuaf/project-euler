from timeit import default_timer as timer
import itertools


def to_int(n):
    return int(''.join(map(str, n)))  # turns [1, 2, 3] into 123

start = timer()
products = set()
target = list(range(1, 10))
combos = itertools.permutations(target, 5)

for combo in combos:
    product = to_int(combo[:2]) * to_int(combo[2:])
    # grouping 2-digit, 3-digit
    if sorted(list(combo) + list(map(int, str(product)))) == target:
        products.add(product)  # sort and compare
    product = to_int(combo[:1]) * to_int(combo[1:])
    # now 1-digit, 4-digit
    if sorted(list(combo) + list(map(int, str(product)))) == target:
        products.add(product)  # sort and compare again

ans = sum(list(products))
elapsed_time = (timer() - start) * 1000  # s --> ms

print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
