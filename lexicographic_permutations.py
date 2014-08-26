"""What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
from itertools import permutations
from timeit import default_timer as timer


start = timer()
current_number = 0
for x in permutations(range(10)):
    current_number += 1
    if current_number == 1000000:
        ans = ''.join(map(str, list(x)))
        break

elapsed_time = (timer() - start) * 1000
print("\nFound %d as the millionth permutation in %d ms.\n"
      % (int(ans), elapsed_time))
