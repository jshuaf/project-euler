from timeit import default_timer as timer


def spiral_diag_sum(n):  # finds sum of corners of Ulam spiral
    if n < 1 or n % 2 == 0:
        raise ValueError("argument must be an odd-valued integer >= 1")
    elif n == 1:
        return 1
    else:
        numbers = [1]
        numbers_needed = 2 * n - 1
        increment = 2
        while len(numbers) < numbers_needed:
            for p in range(4):
                numbers.append(numbers[-1] + increment)
            increment += 2
        return sum(numbers)

start = timer()
ans = spiral_diag_sum(1001)
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
