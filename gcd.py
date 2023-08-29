import sys
def gcd(a, b):
	r = sys.maxsize
	if a < b:
		a, b = b, a
	
	while True:	
		r = a % b
		if r == 0:
			return b
		a = b
		b = r


print(gcd(10, 5))