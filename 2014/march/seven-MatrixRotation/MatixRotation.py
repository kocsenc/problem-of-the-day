import unittest
import random
__author__ = 'Kocsen'

# Matrix Rotation for NxN Matris

def gen_matrix(n):
    matrix = [[] for i in range (n)]
    for x in matrix:
        for y in range(n):
            x.append(random.randint(0,99))

    return matrix

def turn_clockwise(matrix):
    return zip(*matrix[::-1])

def main():
    matrix = gen_matrix(5)
    print(matrix)
    print(turn_clockwise(matrix.__str___()))

if __name__ == "__main__":
    main()
    #unittest.main()


class TestMatrixRotation(unittest.TestCase):
    """ Test Cipher """

    def test_rotation(self):
        self.assertTrue(true)
        pass