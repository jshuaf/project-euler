import math


def factorial_digit_sum(input):
    product = math.factorial(input)
    sum = 0
    for char in str(product):
        sum += int(char)
    return sum

print("\nFound %d as the sum.\n" % factorial_digit_sum(100))
