from timeit import default_timer as timer


def has_single_common_element(list_a, list_b):
    common_list = [value for value in list_a if value in list_b]
    if len(common_list) == 1:
        return common_list[0]
    return False

start = timer()
fractions_that_work = []
for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):  # denom must be > num
        # division will strip off the first digit
        # modulus will strip off the 0th digit
        n_digits = sorted([int(numerator / 10), numerator % 10])
        d_digits = sorted([int(denominator / 10), denominator % 10])
        common = has_single_common_element(n_digits, d_digits)
        if common:
            n_digits.remove(common)
            d_digits.remove(common)
            n_rem = n_digits[0]
            d_rem = d_digits[0]
            if n_rem != 0 and d_rem != 0:
                if float(numerator) / denominator == float(n_rem) / d_rem:
                    fractions_that_work.append([numerator, denominator])
product_of_fractions = [1, 1]
for frac in fractions_that_work:
    product_of_fractions[0] *= frac[0]
    product_of_fractions[1] *= frac[1]

ans = product_of_fractions[1] / product_of_fractions[0]
elapsed_time = (timer() - start) * 1000  # s --> ms

print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
