from itertools import count
from timeit import default_timer as timer


def is_pentagon(x):
    return (((24*x + 1)**0.5 + 1)/6).is_integer()


def is_hexagonal(x):
    return (((8*x + 1)**0.5 + 1)/4).is_integer()

start = timer()
for k in count(286):
    num = k*(k+1)/2
    if is_pentagon(num) and is_hexagonal(num):
        ans = num
        break

elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (num, elapsed_time))
