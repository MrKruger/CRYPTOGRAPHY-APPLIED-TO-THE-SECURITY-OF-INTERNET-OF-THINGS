# this class make encrypt and decrypt
# receiving only one parameter in text and returning the processed text

import numpy as np
import math

class CifraCesar(object):
    def __init__(self):
        # represents a const alpha lenght to make index calculus
        self.__alphabetSize = 26
        # to use decrypt algorithm - start with false value. when true the alg is used
        self.__isDecrypt = False
        # key list for crypt and decrypt calculus
        self.__keys = [
            [5, 17, 25, 10, 18, 24, 6, 4, 9, 19, 20, 14, 22, 15, 7, 23, 3, 16, 1, 12, 2, 8, 21, 13, 11],
            [2, 3, 15, 11, 25, 6, 21, 4, 19, 20, 18, 17, 13, 10, 12, 24, 1, 5, 16, 7, 9, 8, 22, 23, 14],
            [16, 12, 24, 14, 8, 1, 15, 21, 23, 20, 3, 11, 9, 2, 17, 10, 18, 4, 25, 5, 19, 6, 13, 22, 7],
            [24, 10, 23, 20, 12, 17, 7, 3, 1, 8, 16, 15, 11, 25, 22, 14, 18, 13, 19, 6, 4, 9, 21, 5, 2],
            [4, 9, 19, 2, 15, 24, 22, 1, 20, 16, 17, 3, 23, 11, 14, 5, 6, 25, 13, 21, 12, 10, 7, 18, 8],
            [7, 14, 22, 9, 8, 15, 20, 1, 11, 10, 3, 19, 18, 2, 16, 24, 23, 4, 13, 21, 25, 6, 12, 17, 5],
            [21, 10, 19, 14, 13, 11, 2, 9, 18, 8, 25, 20, 1, 22, 23, 15, 24, 7, 16, 17, 4, 6, 3, 5, 12],
            [4, 20, 11, 6, 18, 12, 7, 5, 14, 17, 3, 16, 19, 21, 22, 13, 23, 9, 15, 2, 10, 24, 8, 1, 25],
            [14, 6, 4, 13, 18, 11, 2, 10, 23, 19, 7, 3, 20, 12, 21, 9, 16, 25, 5, 1, 15, 17, 22, 8, 24],
            [23, 12, 17, 6, 9, 1, 4, 18, 5, 10, 11, 2, 16, 14, 22, 20, 8, 15, 13, 24, 3, 7, 25, 21, 19],
            [1, 16, 3, 25, 22, 2, 23, 4, 20, 12, 13, 14, 11, 15, 8, 19, 7, 5, 10, 21, 6, 18, 9, 24, 17],
            [8, 12, 14, 13, 15, 24, 4, 18, 2, 20, 1, 6, 7, 22, 10, 25, 17, 3, 21, 5, 11, 23, 9, 19, 16],
            [20, 10, 6, 19, 7, 17, 9, 11, 2, 8, 14, 23, 18, 12, 16, 25, 5, 1, 4, 13, 24, 22, 3, 21, 15],
            [18, 20, 4, 24, 9, 2, 14, 5, 12, 19, 16, 1, 7, 8, 11, 25, 22, 6, 17, 10, 21, 15, 3, 23, 13],
            [11, 12, 25, 23, 19, 9, 20, 22, 10, 14, 4, 1, 13, 5, 6, 2, 8, 7, 18, 16, 15, 24, 17, 3, 21],
            [25, 4, 22, 21, 24, 13, 11, 6, 1, 18, 2, 17, 8, 20, 12, 16, 5, 14, 19, 3, 9, 23, 15, 7, 10],
            [6, 15, 12, 17, 11, 20, 23, 9, 5, 16, 2, 19, 3, 22, 8, 7, 1, 14, 24, 18, 10, 21, 4, 25, 22],
            [13, 23, 14, 12, 11, 7, 15, 24, 18, 4, 17, 2, 8, 25, 6, 3, 5, 22, 19, 20, 10, 16, 1, 21, 9],
            [17, 14, 12, 13, 1, 24, 4, 18, 15, 3, 16, 10, 20, 22, 21, 9, 2, 25, 5, 19, 11, 23, 8, 7, 6],
            [12, 6, 3, 9, 25, 14, 21, 18, 19, 2, 23, 1, 11, 15, 5, 20, 13, 22, 24, 8, 17, 10, 16, 7, 4],
            [10, 24, 20, 22, 23, 16, 12, 6, 18, 15, 5, 8, 17, 7, 2, 25, 14, 13, 4, 11, 9, 19, 21, 3, 1],
            [19, 1, 21, 14, 11, 3, 20, 4, 2, 17, 13, 24, 12, 9, 23, 25, 16, 15, 5, 10, 22, 6, 8, 7, 18],
            [9, 23, 11, 14, 6, 10, 17, 24, 4, 22, 25, 16, 3, 8, 21, 1, 15, 7, 2, 18, 5, 13, 12, 19, 20],
            [22, 2, 3, 10, 9, 25, 19, 4, 18, 13, 14, 8, 17, 24, 12, 1, 15, 21, 16, 20, 5, 7, 23, 11, 6],
            [3, 1, 13, 21, 12, 16, 8, 18, 11, 4, 10, 17, 24, 2, 15, 20, 14, 5, 22, 19, 9, 6, 25, 7, 23],
            [22, 6, 8, 1, 11, 17, 3, 5, 18, 16, 25, 14, 9, 19, 13, 23, 12, 20, 7, 10, 15, 4, 21, 2, 24],
            [24, 20, 18, 21, 11, 9, 23, 22, 13, 1, 15, 6, 3, 25, 17, 12, 8, 7, 5, 19, 10, 4, 16, 2, 14],
            [14, 16, 4, 11, 24, 12, 25, 19, 5, 6, 7, 10, 20, 15, 18, 1, 8, 21, 17, 22, 3, 23, 2, 9, 13],
            [1, 8, 18, 7, 10, 15, 5, 12, 24, 17, 19, 25, 9, 20, 2, 6, 23, 4, 22, 11, 16, 14, 13, 21, 3],
            [24, 10, 23, 20, 12, 17, 7, 3, 1, 8, 16, 15, 11, 25, 22, 14, 18, 13, 19, 6, 4, 9, 21, 5, 2],
            [18, 14, 25, 7, 4, 10, 24, 15, 5, 17, 9, 23, 2, 12, 19, 1, 20, 6, 3, 21, 11, 22, 13, 8, 16],
            [5, 8, 24, 7, 20, 10, 19, 3, 16, 23, 1, 25, 21, 6, 9, 13, 4, 15, 14, 22, 18, 11, 17, 2, 12],
            [24, 20, 9, 13, 25, 23, 6, 16, 21, 2, 1, 4, 17, 5, 19, 3, 12, 11, 8, 15, 7, 10, 14, 22, 18],
            [22, 9, 16, 13, 11, 3, 15, 8, 19, 4, 10, 7, 6, 5, 12, 23, 25, 18, 1, 20, 14, 17, 2, 21, 24],
            [19, 5, 6, 22, 24, 1, 11, 23, 25, 9, 20, 13, 8, 16, 2, 21, 18, 7, 3, 12, 4, 10, 17, 15, 14],
            [22, 10, 11, 15, 2, 18, 5, 4, 21, 17, 8, 6, 1, 3, 7, 23, 14, 19, 20, 13, 24, 16, 9, 12, 25],
            [3, 17, 9, 1, 15, 10, 5, 24, 16, 8, 20, 25, 13, 18, 12, 11, 14, 21, 23, 19, 4, 2, 22, 6, 7],
            [4, 19, 10, 14, 23, 21, 7, 3, 13, 25, 24, 20, 1, 16, 5, 6, 11, 18, 22, 9, 8, 15, 2, 12, 17],
            [20, 10, 6, 19, 7, 17, 9, 11, 2, 8, 14, 23, 18, 12, 16, 25, 5, 1, 4, 13, 24, 22, 3, 21, 15],
            [15, 10, 3, 1, 8, 11, 18, 24, 5, 9, 12, 21, 16, 6, 14, 22, 25, 2, 7, 17, 23, 19, 4, 20, 13],
            [3, 20, 12, 1, 23, 2, 19, 6, 17, 7, 24, 16, 21, 5, 18, 14, 11, 8, 25, 10, 22, 13, 4, 9, 15],
            [25, 4, 22, 21, 24, 13, 11, 6, 1, 18, 2, 17, 8, 20, 12, 16, 5, 14, 19, 3, 9, 23, 15, 7, 10],
            [2, 6, 25, 16, 8, 13, 17, 15, 12, 9, 19, 10, 23, 14, 3, 20, 4, 1, 11, 7, 21, 22, 18, 24, 5],
            [13, 23, 14, 12, 11, 7, 15, 24, 18, 4, 17, 2, 8, 25, 6, 3, 5, 22, 19, 20, 10, 16, 1, 21, 9],
            [11, 13, 5, 20, 21, 19, 14, 22, 4, 12, 25, 24, 1, 2, 8, 6, 7, 15, 16, 18, 23, 10, 9, 17, 3],
            [2, 24, 7, 6, 25, 13, 18, 23, 15, 5, 12, 22, 1, 19, 16, 11, 8, 3, 10, 20, 17, 21, 9, 4, 14],
            [10, 24, 20, 22, 23, 16, 12, 6, 18, 15, 5, 8, 17, 7, 2, 25, 14, 13, 4, 11, 9, 19, 21, 3, 1],
            [19, 20, 1, 6, 14, 22, 16, 17, 3, 13, 9, 15, 21, 10, 8, 4, 7, 12, 18, 23, 24, 2, 11, 5, 25],
            [4, 11, 7, 24, 6, 25, 20, 13, 12, 10, 1, 19, 3, 15, 5, 14, 21, 2, 18, 16, 8, 22, 23, 17, 9],
            [15, 12, 19, 7, 24, 18, 13, 5, 3, 1, 11, 16, 2, 22, 4, 14, 17, 6, 25, 21, 23, 20, 9, 10, 8],
            [25, 7, 9, 16, 11, 8, 12, 4, 17, 24, 14, 2, 20, 10, 19, 6, 1, 3, 21, 13, 15, 23, 22, 5, 18],
            [20, 8, 16, 9, 21, 24, 19, 23, 22, 4, 11, 7, 15, 10, 6, 14, 2, 18, 1, 12, 5, 17, 13, 25, 3]
        ]
        # represent a key that are used in calc
        self.__key = 0

    #############################################
    #   H   E   L   P    E    R   S
    #############################################

    # convert text to char list
    def __convertTextToList(self, text):
        letterList = []
        for letter in range(len(text)):
            letterList.append(text[letter])
        return letterList

    # get a perfect matrix
    def __getPerfectMatrix(self, message):
        msg_size = len(message)
        sqrt_msg_size = int(math.sqrt(msg_size))
        num_rounded = int(math.ceil(math.sqrt(msg_size)))

        zeros_matrix = np.zeros((num_rounded * num_rounded) - msg_size, dtype=np.int)
        zeros_matrix_list = zeros_matrix.tolist()

        perfect_matrix = np.array(message + zeros_matrix_list).reshape((
            num_rounded,
            num_rounded
        ))

        square_numbers = [x * x for x in range(76)]                # get some square numbers
        if msg_size in square_numbers:
            matrix = np.array(message).reshape((sqrt_msg_size, sqrt_msg_size))
        else:
            matrix = perfect_matrix

        return matrix

    # process the text and return a new list with index changes
    def __sortMatrix(self, calc, matrix):
        self.__key = - self.__keys[0][0] if self.__isDecrypt else self.__keys[0][0]  # first key, positive or not?
        sorted_matrix = calc(matrix, self.__key)

        for i in range(1, 25):
            for j in range(52):
                if self.__isDecrypt:
                    self.__key = - self.__keys[j][i]                        # reverse algorithm with negative key
                else:
                    self.__key = self.__keys[j][i]                          # normal algorithm with positive key

                sorted_matrix = calc(sorted_matrix, self.__key)  # sort matrix with the key in the Keys list

        return sorted_matrix

    # transpose matrix data
    def __handleText(self, calc, text):
        for _ in range(25):
            _list = self.__convertTextToList(text)                              # convert text as char list
            perfect_matrix = self.__getPerfectMatrix(_list)                     # convert list to perfect matrix (x*x)
            transposed_matrix = perfect_matrix.transpose().flatten().tolist()   # transpose and convert to list again kk
            sorted_matrix = self.__sortMatrix(calc, transposed_matrix)
        return sorted_matrix

    # Encrypts only alpha texts
    def encrypt(self, text):
        self.__isDecrypt = False                                                # normal alg. not use negative keys
        encrypted_text = self.__handleText(self.__calc, text)
        return encrypted_text                  # pass a positive key

    # Decrypts only alpha texts
    def decrypt(self, text):
        self.__isDecrypt = True                                                 # set decrypt keys negative.
        decrypted_text = self.__handleText(self.__calc, text)
        return decrypted_text

    # base for the two ways - encrypt and decrypt are similar
    def __calc(self, text, key):
        new_text = ""
        for letter in text:
            if letter.isalpha():
                index = ord(letter)                                              # get the order of a letter in alphabet
                index += key

                if letter.isupper():
                    if index > ord("Z"):
                        index -= self.__alphabetSize
                    elif index < ord("A"):
                        index += self.__alphabetSize
                else:
                    if index > ord("z"):
                        index -= self.__alphabetSize
                    elif index < ord("a"):
                        index += self.__alphabetSize

                new_text += chr(index)                                           # get char from alphabet with a index
            else:
                new_text += letter                                               # get normal char
        return new_text
