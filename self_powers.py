from timeit import default_timer as timer


def sum_self_powers(n):
    return sum(k**k for k in range(1, n + 1))

start = timer()
ans = str(sum_self_powers(1000))[-10:]
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (int(ans), elapsed_time))
