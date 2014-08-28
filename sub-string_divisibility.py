from itertools import permutations
from primes import primes_upto
from timeit import default_timer as timer
from copy import deepcopy


def generate_multiples(n):
    multiples = set()
    for x in range(1000//n):
        product = str(x*n)
        multiples.add(product)
    return multiples

start = timer()
primes = primes_upto(17)
multiples_start = {k: {} for k in primes}
multiples_end = {k: {} for k in primes}
digits = set((str(x) for x in range(10)))
for x in primes[::-1]:
    current_multiples = generate_multiples(x)
    for multiple in current_multiples:
        string_version = str(multiple)
        while len(string_version) < 3:
            # add preceding zeros to preserve
            # three-digit length
            string_version = '0' + string_version
        end = string_version[1:]
        start = string_version[:2]
        if x != 17:
            multiples_end[x].setdefault(end, []).append(string_version)
        else:
            multiples_start[x].setdefault(start, []).append(string_version)

pandigitals = {}
pandigitals2 = deepcopy(multiples_start[17])
for prime in primes[-2::-1]:
    pandigitals = deepcopy(pandigitals2)
    pandigitals2 = {}
    for part, pandigital_list in pandigitals.items():
        if part in multiples_end[prime]:
            for pandigital in pandigital_list:
                for match in multiples_end[prime][part]:
                    new_num = match + pandigital[2:]
                    pandigitals2.setdefault(match[:2], []).append(new_num)
del pandigitals

total = 0
for candidate_list in pandigitals2.values():
    for candidate in candidate_list:
        current_digits = set(candidate)
        if len(current_digits) == len(candidate):
            (last_digit,) = digits - current_digits
            total += int(last_digit + candidate)

elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (total, elapsed_time))
