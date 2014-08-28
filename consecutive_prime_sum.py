from primes import primes_upto, test
from timeit import default_timer as timer


def most_consec_prime_sum_upto(n):
    primes = primes_upto(n)
    temp_total = 0
    for index, prime in enumerate(primes):
        if temp_total >= 10**6:
            primes = primes[:index + 1]
            break
        else:
            temp_total += prime

    for sequence_len in range(len(primes), 0, -2):
        for index in range(len(primes) - sequence_len):
            total = sum(primes[index:(index + sequence_len - 1)])
            if test(total):
                return total


start = timer()
ans = most_consec_prime_sum_upto(10**6)
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
