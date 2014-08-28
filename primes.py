import math

def test(num): # checks if a number is prime
	if num <= 3:
		if num <= 1:
			return False
		return True
	if not num%2 or not num%3:
		return False
	for i in range(5, int(num**0.5) + 1, 6):   
		if not num%i or not num%(i + 2):
			return False
	return True

def factorization(n): # returns prime factorization of # in list
	step = lambda x: 1 + x*4 - (x//2)*2
	maxq = math.floor(math.sqrt(n))
	d = 1
	q = n % 2 == 0 and 2 or 3 
	while q <= maxq and n % q != 0:
		q = step(d)
		d += 1
	res = []
	if q <= maxq:
		res.extend(factorization(n//q))
		res.extend(factorization(q)) 
	else: res=[n]
	return res

def primes_upto(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]
	
def generate(): # generates all prime numbers
	import heapq
	for p in [2,3,5,7]: yield p                 # base wheel primes
	gaps1 = [ 2,4,2,4,6,2,6,4,2,4,6,6,2,6,4,2,6,4,6,8,4,2,4,2,4,8 ]
	gaps = gaps1 + [ 6,4,6,2,4,6,2,6,6,4,2,4,6,2,6,4,2,4,2,10,2,10 ] # wheel2357
	def wheel_prime_pairs():
		yield (11,0); bps = wheel_prime_pairs() # additional primes supply
		p, pi = next(bps); q = p * p            # adv to get 11 sqr'd is 121 as next square to put
		sieve = {}; n = 13; ni = 1              #   into sieve dict; init cndidate, wheel ndx
		while True:
			if n not in sieve:                  # is not a multiple of previously recorded primes
				if n < q: yield (n, ni)         # n is prime with wheel modulo index
				else:
					npi = pi + 1                # advance wheel index
					if npi > 47: npi = 0
					sieve[q + p * gaps[pi]] = (p, npi) # n == p * p: put next cull position on wheel
					p, pi = next(bps); q = p * p  # advance next prime and prime square to put
			else:
				s, si = sieve.pop(n)
				nxt = n + s * gaps[si]          # move current cull position up the wheel
				si = si + 1                     # advance wheel index
				if si > 47: si = 0
				while nxt in sieve:             # ensure each entry is unique by wheel
					nxt += s * gaps[si]
					si = si + 1                 # advance wheel index
					if si > 47: si = 0
					sieve[nxt] = (s, si)            # next non-marked multiple of a prime
			nni = ni + 1                        # advance wheel index
			if nni > 47: nni = 0
			n += gaps[ni]; ni = nni             # advance on the wheel
	for p, pi in wheel_prime_pairs(): yield p   # strip out indexes
	
def GCD(m, n):
	while n != 0:
		m, n = n, m - n*(m // n)
	return m
	
