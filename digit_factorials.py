from math import factorial as fact
from timeit import default_timer as timer


start = timer()
# pre-calculate products
factorials = [fact(x) for x in range(10)]
total_sum = 0

for n in range(10, 100000):  # 9999999 is way more than its fact-sum
    digits = n
    current_total = 0
    while digits > 0:
        current_digit = digits % 10
        if current_total > n:
            break
        current_total += factorials[current_digit]
        digits //= 10
    if current_total == n:
        total_sum += n


ans = total_sum
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
