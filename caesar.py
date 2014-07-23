#Caesar cipher
#Author: Eden
from string import maketrans, translate, lowercase
import sys

if len(sys.argv) != 3:
    print "Usage: " + sys.argv[0] + " plaintext placestoshift"
    exit(1)
isLower = sys.argv[1][0].islower() #if the output is piped the it stays in the correct case
plaintext = sys.argv[1].lower()
shifter = int(sys.argv[2]) #cast to use as slice index

alpha = lowercase
shiftedAlpha = alpha[shifter:] + alpha[:shifter]
table = maketrans(alpha, shiftedAlpha)

ciphertext = plaintext.translate(table)
if isLower:
    print ciphertext
else :
    print ciphertext.upper()
