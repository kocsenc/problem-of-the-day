# Kocsen Chung
# Problem of The day
# http://www.problemotd.com/problem/letters-to-numbers/

# Add these
# B P P D Q P C
# P R P D Q B D
# -----------------------
# X V D W T R C

def main():
	"""
	Changed string values to its ordinal values using the convert method and ads them
	"""
	FIRST = 'BPPDQPC'
	SECOND = 'PRPDQBD'

	answer = convert(FIRST) + convert(SECOND)
	print(answer)
	return asnwer

def convert(input_string):
	"""
	Returns int value of a coded string
	"""
	res = ''
	for char in input_string:
		res += str(ord(char)%65)

	return int(res)


if __name__ == "__main__":
	main()