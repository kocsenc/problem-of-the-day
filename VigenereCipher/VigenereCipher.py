import unittest

__author__ = 'Kocsen'
# Vigenere Cipher
# see problem.txt for full problem

# Needs key and message
# Key: REDDIT
# Message: TODAYISMYBIRTHDAY

ordinal_difference = 65


def cipher(key, message):
    key = key.upper()
    lenkey = len(key)

    message = message.upper()
    result = ''

    for i in range(len(message)):
        cipher_index = (alpha_pos(key[i % lenkey]) + alpha_pos(message[i])) % 26
        result += chr(ordinal_difference + cipher_index)
    return result


def decipher(encrypted):
    for char in encrypted:
        pass


def alpha_pos(char):
    return ord(char) - ordinal_difference


if __name__ == "__main__":
    unittest.main()


class TestVigenereCipher(unittest.TestCase):
    """ Test Cipher """

    def test_cipher(self):
        self.assertEqual("KSGDGBJQBEQKKLGDG", cipher("REDDIT", "TODAYISMYBIRTHDAY"))
        # From wikipedia
        self.assertEqual("CSASTPKVSIQUTGQUCSASTPIUAQJB", cipher("ABCD", "CRYPTOISSHORTFORCRYPTOGRAPHY"))
