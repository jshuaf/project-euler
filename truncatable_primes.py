from primes import test as is_prime
from itertools import product
from timeit import default_timer as timer


def is_trunc(list_num):
    num = ''.join(map(str, list_num))  # turn (1, 2, 3) into 123
    if is_prime(int(num)):
        primes.append(int(num))
        for k in range(1, len(num)):
            if not is_prime(int(num[k:])) or not is_prime(int(num[:k])):
                return False
        return True
    return False


start = timer()
primes = []
data = {"count": 0, "length": 2, "sum": 0}
while data["count"] < 11:
    for combo in product([1, 2, 3, 5, 7, 9], repeat=data["length"]):
        if is_trunc(combo):
            data["count"] += 1
            data["sum"] += int(''.join(map(str, list(combo))))
    data["length"] += 1

ans = data["sum"]
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
