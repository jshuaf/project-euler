from primes import primes_upto
from timeit import default_timer as timer


start = timer()
distinct_prime_factors = [0] * 300001
primes = primes_upto(300000)
for prime in primes:
    for multiplier in range(1, 300000//prime + 1):
        distinct_prime_factors[prime*multiplier] += 1

streak = 0
for index, fact_num in enumerate(distinct_prime_factors):
    if fact_num == 4:
        if streak == 3:
            ans = index - 3
            break
        else:
            streak += 1
    else:
        streak = 0

elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
