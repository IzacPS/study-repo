import sys
def gcd(a, b):
	r = sys.maxsize
	if a < b:
		a, b = b, a
	
	while b != 0:	
		a = b
		b = a % b

	return a

print(gcd(10, 5))