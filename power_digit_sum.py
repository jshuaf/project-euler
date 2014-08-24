def sum_of_digits(num):
    total = 0
    for x in str(num):
        total += int(x)
    return total

print("\nFound %d as the sum.\n" % sum_of_digits(2**1000))
