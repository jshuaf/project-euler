from itertools import count
from timeit import default_timer as timer


def is_pentagonal(x):
    return (((24*x + 1)**0.5 + 1)/6).is_integer()


def pentagonal_size(k):
    return k*(3*k - 1)/2  # formula

pentagon_nums = [pentagonal_size(x) for x in range(0, 10000)]

start = timer()
found = False
for k in count(3):
    for m in range(1, k + 1):
        k1 = pentagon_nums[k]
        m1 = pentagon_nums[m]
        if is_pentagonal(k1 + m1) and is_pentagonal(k1 - m1):
            found = k1 - m1
            break
    if found:
        break

ans = found
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms." % (ans, elapsed_time))
