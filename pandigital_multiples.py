from timeit import default_timer as timer


def create_pandigital_multiple(original_number):
    num = str(original_number)
    temp = 2
    while len(num) < 9:
        num += str(original_number * temp)
        temp += 1
    if len(num) == 9:
        if sorted(num) == digits:
            return int(num)
        else:
            return False
    return False

start = timer()
ans = 0
digits = [str(i) for i in range(1, 10)]
for n in range(9, 10**5):
    if int(str(n)[:2]) >= 91 and int(str(n)[:2]) <= 98:
        pandigital = create_pandigital_multiple(n)
        if pandigital > ans:
            ans = pandigital

elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
