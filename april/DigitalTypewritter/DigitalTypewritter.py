# Kocsen Chung
# Problem of the day - Digital Typewritter
# April 22, 2014
import sys
import fileinput


def main():
    f = open('output.txt', 'w')
    master_out = ""

    start_end_sequence = False

    print("Typewritter | Start writing")
    while (True):
        line = input()
        print("you have inputted: " + line)
        # Listener for ending typewriter
        if line == '':
            start_end_sequence = True
            print("Started end sequence")
        else:
            start_end_sequence = False
            master_out += (line + "\n")

        if start_end_sequence and line == ".":
            print("You are done here")
            break

    f.write(master_out)
    f.close()


if __name__ == "__main__":
    main()

