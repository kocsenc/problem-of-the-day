# Kocsen Chung

def find_chorus(filename):
	# Dictionary that keeps track of repeated lines
	group = {}
	largest = 0 		   # Counter for group repetitions
	potential_chorus = ''  # Temp variable represents different sections
	chorus = ''            # Variable set when chorus is found
	with open(filename,'r') as song:
		# Where the magic happens
		# It will split the lyrics by an empty line which signifies
		# the end of a section (verse, chorus).
		# Using a dictionary it will keep track of all these sections
		# and keep count. Highest count = chorus.
		for line in song.readlines():
			if line == '' or line == '\n':
				# We now have a section. Lets check if its in our group
				# of sections
				if potential_chorus in group:
					# It is! Let's ++ its count and check if its repeated the most
					group[potential_chorus] += 1
					if group[potential_chorus] > largest:
						largest = group[potential_chorus]
						chorus = potential_chorus
				else:
					# The section is new, let's add it
					group[potential_chorus] = 1
				
				# Clear group
				potential_chorus = ''
			else:
				potential_chorus += line
				

	print("I think the potential chorus is:\n" + chorus)
	print("With a count of %d", largest)

if __name__ == "__main__":
	find_chorus("song.txt")
