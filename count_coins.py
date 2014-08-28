from timeit import default_timer as timer


def count_coins(sum, coins):
    ways_to_make = [0 for _ in range(sum + 1)]
    ways_to_make[0] = 1
    for coin in coins:
        for t in range(sum + 1):
            if t >= coin:
                ways_to_make[t] += ways_to_make[t - coin]

    return ways_to_make[sum]

start = timer()
ans = count_coins(200, [1, 2, 5, 10, 20, 50, 100, 200])
elapsed_time = (timer() - start) * 1000  # s --> ms

print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
