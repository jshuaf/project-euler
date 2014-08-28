from timeit import default_timer as timer


def digit_powers(exponent):
    if exponent <= 1:
        return "The exponent must be at least 2."
    powdigits = [i**exponent for i in range(10)]
    total_sum = 0
    upper_bound = (exponent + 1) * powdigits[9]
    for number in range(10, upper_bound + 1):
        partialsum = tempnum = number
        while tempnum:
            partialsum -= powdigits[tempnum % 10]
            tempnum //= 10
        if not partialsum:
            total_sum += number
    return total_sum

start = timer()
ans = digit_powers(5)
elapsed_time = (timer() - start) * 1000  # s --> ms

print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
