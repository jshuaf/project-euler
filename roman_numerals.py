from timeit import default_timer as timer

numeral_values = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
}
represents = {v:k for k, v in numeral_values.items()}
numerals = open('roman.txt').readlines()
numerals = [x[:-1] for x in numerals[:-1]]
numerals.append('XXXXVIIII')

def min_roman_numeral(numeral):
	numeral_value = 0
	for index, x in enumerate(list(numeral)):
		if index != len(numeral) - 1:
			if numeral_values[x] < numeral_values[numeral[index + 1]]:
				numeral_value -= numeral_values[x]
			else:
				numeral_value += numeral_values[x]
		else:
			numeral_value += numeral_values[x]
	numeral_value = str(numeral_value)
	numeral_representation = []
	if len(numeral_value) >= 4:
		for thousand in range(int(numeral_value[:-3])):
			numeral_representation.append('M')
		for index in range(-3, 0):
			digit = int(numeral_value[index])
			place = 10**(-index-1)
			if digit <= 3:
				for _ in range(digit):
					numeral_representation.append(represents[place])
			elif digit == 4:
				numeral_representation.extend([represents[place], represents[place*5]])
			elif digit == 5:
				numeral_representation.append(represents[place*5])
			elif digit <= 8:
				numeral_representation.append(represents[place*5])
				for _ in range(digit - 5):
					numeral_representation.append(represents[place])
			elif digit == 9:
				numeral_representation.extend([represents[place], represents[place*10]])
	if len(numeral_value) <= 3:
		for index in range(-(len(numeral_value)), 0):
			digit = int(numeral_value[index])
			place = 10**(-index-1)
			if digit <= 3:
				for _ in range(digit):
					numeral_representation.append(represents[place])
			elif digit == 4:
				numeral_representation.extend([represents[place], represents[place*5]])
			elif digit == 5:
				numeral_representation.append(represents[place*5])
			elif digit <= 8:
				numeral_representation.append(represents[place*5])
				for _ in range(digit - 5):
					numeral_representation.append(represents[place])
			elif digit == 9:
				numeral_representation.extend([represents[place], represents[place*10]])
			
	return ''.join(numeral_representation)

start = timer()
ans = sum(len(numeral) - len(min_roman_numeral(numeral)) for numeral in numerals)
elapsed_time = (timer() - start) * 1000 # s --> ms
print("\nIn %d ms, found %d characters saved.\n" % (elapsed_time, ans))

