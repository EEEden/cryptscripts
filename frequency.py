#!/usr/bin/python
import sys
import string

#alphabet sorted in order of frequency mapped to the % occurence
#Source: The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography
sortedAlpha = {"e": 12.7, "t": 9.1, "a": 8.2, "o": 7.5, "i": 7.0, "n": 6.7, "s": 6.3, "h": 6.1, "r": 6.0, "d": 4.3, "l": 4.0, "c": 2.8, "u": 2.8, "m": 2.4, "w": 2.4, "f": 2.2, "g": 2.0, "y": 2.0, "p": 1.9, "b": 1.5, "v": 1.0, "k": 0.8, "j": 0.2, "x": 0.2, "q": 0.1, "z": 0.1};

#return a frequency dictionary in the form:
#{ "a" : 0 } where the key is a letter of the alphabet and the value is the frequency of said letter
def getFreqDict (message):
    alphaFreq = dict.fromkeys(sortedAlpha.keys(), 0)

    for letter in message:
        if letter in sortedAlpha.keys():
            alphaFreq[letter]+=1

    return alphaFreq

def main(message):
    freqDict = getFreqDict(message)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage " + sys.argv[0] + " message"
        exit(1)
    message = sys.argv[1]
    main(message)
