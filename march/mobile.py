# Kocsen Chung

#Mobile 6
#Today's goal is to try and find an integer where the digit in the 
# ones column is a 6 and when the 6 is moved to the front of the number, 
# the number becomes 4 times the value of the starting number.


def mobile():
	LIMIT = 999999
	for number in range(6, LIMIT, 10):
		num_str = str(number)
		intified = int("6" + num_str[:-1])
		if intified == number * 4:
			print("Seems like we found it!")
			print(num_str)
			break



if __name__ == "__main__":
	mobile()

