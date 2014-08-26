def first_fib_with_digit_number(length):
    f0, f1 = 1, 1
    count = 2
    while len(str(f1)) != length:
        f0, f1 = f1, f0 + f1
        count += 1
    return count

ans = first_fib_with_digit_number(1000)
print("\nFound %d as the first term with 1000 digits\n" % ans)
