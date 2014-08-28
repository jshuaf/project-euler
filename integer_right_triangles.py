from timeit import default_timer as timer


def find_pythagorean_triples(perimeter):
    count = 0
    for a in range(3, perimeter // 2 - 1):  # triangle inequality
        c = (a**2 + (perimeter - a)**2) / (2*(perimeter - a))
        # derived formula
        b = (c**2 - a**2)**0.5
        if b.is_integer() and a + b + c == perimeter:
            count += 1
    return count


def find_most_solutions_upto(limit):
    return max(range(limit//2, limit + 1), key=find_pythagorean_triples)


start = timer()
ans = find_most_solutions_upto(1000)
elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
