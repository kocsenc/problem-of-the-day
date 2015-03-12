# Kocsen Chung

# 1000 Barrels
# 1 is poisoned 
# poison takes 7 days to kill
# you have 10 humans to test 
# you have 10 days to test
# you want 999 barrels at the end
import random

def main():
	barrels = []
	for i in range (1000):
		barrels.append(Barrel(i))
	
	peeps = []
	for i in range(10):
		peeps.append(Person(i))

	# Poison random barrel
	barrel_index = random.randint(0,999)
	print("poisoning barrel #" + str(barrel_index))
	barrels[barrel_index].poisoned = True

	# separate in groups of 100
	for barrel in barrels[0:99]:
		pass
class Barrel():
	def __init__(self, id, poisoned=False):
		self.id = id
		self.poisoned = poisoned

	def taste(self):
		if self.poisoned:
			return False 
		return True

class Person():
	def __init__(self, id):
		self.id = id	
		self.days_living = 7

if __name__ == "__main__":
	main()
