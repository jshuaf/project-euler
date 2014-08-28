from timeit import default_timer as timer


def is_palindrome(s):
    s = str(s)
    return s == s[::-1]


def sum_double_base_palindromes_under(limit):
    total = 0
    for n in range(limit):
        normal = is_palindrome(n)
        if normal:
            binary = is_palindrome(bin(n)[2:])
            if binary:
                total += n
    return total

start = timer()
ans = sum_double_base_palindromes_under(1000000)
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
