# Kocsen Chung

# When given 3 integers it returns the smallest integer of the 3 without using
# comparison operators
import math

def main(a,b,c):
	ary = [a,b,c]	
	res = a-b
	if is_neg(res):
		# Means B greater than A
		res = b-c
		if is_neg(res):
			return c
		else:
			return b
	else:
		# A > B
		res = a-c
		if is_neg(res):
			return c
		else:
			return a


def is_neg(x):
	if len(str(int(math.fabs(x)))) != len(str(int(x))):
		return True
	return False


if __name__ == "__main__":
	a = 4
	b = 123
	c = 3

	print(str(main(a,b,c)))
