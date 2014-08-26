"""
How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# Jan 01 1901 = 2; tuesday

firstdays = [2]
months_with_31 = [1, 3, 5, 7, 8, 10, 12]
for year in range(1901, 2001):
    for m in range(1, 13):
        if m in months_with_31:
            firstdays.append(((firstdays[-1] + 31) % 7))
        elif m == 2:
            if year % 4 == 0:
                if year % 100 == 0 and year % 400 != 0:
                    firstdays.append(((firstdays[-1] + 28) % 7))
                else:
                    firstdays.append(((firstdays[-1] + 29) % 7))
            else:
                firstdays.append(((firstdays[-1] + 28) % 7))
        else:
            firstdays.append(((firstdays[-1] + 30) % 7))

ans = sum(x == 0 for x in firstdays)
print("\nFound %d months.\n" % ans)
