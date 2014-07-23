#Brute force caesar cipher by printing all possible shift results allowing plaintext to be found through visual inspection
#Author: Eden

from string import translate, maketrans, lowercase
import sys

if len(sys.argv) != 2:
    print "Usage: " + sys.argv[0] + " ciphertext"
    exit(1)
isLower = sys.argv[1][0].islower()
ciphertext = sys.argv[1].lower()

alpha = lowercase
shiftedAlpha = ""
plaintext = ""
table = None
for i in range(len(alpha)):
    shiftedAlpha = alpha[i:] + alpha[:i]
    table = maketrans(alpha, shiftedAlpha)
    plaintext = ciphertext.translate(table)
    if isLower:
        print plaintext
    else :
        print plaintext.upper()
