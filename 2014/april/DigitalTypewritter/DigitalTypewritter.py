# Kocsen Chung
# Problem of the day - Digital Typewritter
# April 22, 2014
import sys
import fileinput
import webbrowser

FNAME = 'output.txt'
MAXL = 72
def main():
	f = open(FNAME, 'w')
	master_out = ""

	start_end_sequence = False
	print("Typewritter | Start writing")
	while (True):
		line = input()

		if line == '.' and start_end_sequence:
			break

		# Listener for ending typewriter
		if line == '':
			start_end_sequence = True
		else:
			start_end_sequence = False
			if len(line) > MAXL:
				print("\tERROR: Limit of characters per line is 72, TRUNCATING")
				master_out += (line[:MAXL] + '\n')
			else:
				master_out += (line + '\n')

	f.write(master_out)
	f.close()

	# Printing out file
	print("\nTypewriter | Openning result file")
	webbrowser.open(FNAME)

if __name__ == "__main__":
	main()

