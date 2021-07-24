import sys
from time import gmtime, strftime
import math


def _2Encrypt(_2input):
    _2Output = ''
    if ((len(_2input) < 12) or (_2input.isalnum() != True)):
        print("The length of reference ID cannot be less than 12 or any special characters.")
    else:
        for index in _2input:
            if index.isalpha() == True:
                _2Output = _2Output + str((ord(index)))
            elif index.isdigit() == True:
                _2Output = _2Output + str(chr(int(index)))
        print("The encrypted Reference ID is:", _2Output)

def _2Decrypt(_2input):
    _2Output = ''
    if ((len(_2input) < 12) or (_2input.isalnum() != True)):
        print("The length of reference ID cannot be less than 12 or any special characters.")
    else:
        for index in _2input:
            if index.isalpha() == True:
                _2Output = _2Output + str((ord(index)))
            elif index.isdigit() == True:
                _2Output = _2Output + str(chr(int(index)))
        print("The encrypted Reference ID is:", _2Output)

if __name__ == "__main__":
    option = int(input("Enter Option 1 for Encryption or 2 for Decryption:"))
    if option == 1:
        _2Input = input("Enter Reference ID for Encryption: ")
        _2Encrypt(_2Input)
    if option == 2:
        _2Input = input("Enter Decrypted Reference ID: ")
        _2Decrypt(_2Input)