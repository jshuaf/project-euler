namestxt = open('names_scores.txt', 'r')
names = namestxt.read()
names = sorted(names.split(','))
scoressum = 0
for index, name in enumerate(names):
    position = index + 1
    value = sum((ord(char) - 64) for char in name[1:-1])
    scoressum = scoressum + (position * value)

print("\nFound the sum of the scores as %d.\n" % scoressum)
