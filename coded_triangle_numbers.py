from timeit import default_timer as timer


def is_triangle_word(word):
    return sum((ord(k) - 64) for k in word) in triangle_nums


start = timer()
words = open('triangle_words.txt', 'r').read().split(',')
triangle_nums = [x*(x+1)/2 for x in range(26*int(len(max(words, key=len))))]
ans = 0
for word in words:
    if is_triangle_word(word[1:-1]):
        ans += 1

elapsed_time = (timer() - start) * 1000  # s --> ms
print("\nFound %d in %d ms.\n" % (ans, elapsed_time))
