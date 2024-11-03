import sympy
import string
import math

class cryptRSA(object):
    def __init__(self, e, p, q):
        self.p = p
        self.q = q
        self.n = None
        self.phi = None
        self.e = e
        self.d = None
        self.c = None
        self.firstNum = False


    def getN(self):
        return self.n

    def getD(self):
        return self.d

    def getE(self):
        return self.e

    #Section A
    # Generate prime numbers

    def primeNumbers(self):
        self.p = sympy.nextprime(self.p)
        self.q = sympy.nextprime(self.q)

    # Calcul n and phi(n)

    def numbersNandPhi(self):
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

    # Is prime number
    def isPrime(self):
        return math.gcd(self.n, self.phi) == 1

    # Generate private key

    def privateKey(self):
        self.d = sympy.invert(self.e, self.phi)

    #Print public and private key
    def publicPrivateKey(self):
        self.primeNumbers()
        self.numbersNandPhi()

        if self.isPrime():
            self.privateKey()

            print("Public key (n,e): (" + str (self.n) + "," + str (self.e) + ")" )
            print("Private key (d): (" + str(self.d) + ")" )
        else:
            print("Not a prime numbers within each other")

    # Section B

    #Text to ASCII
    def textToAscii(self, s):
        if 'a' <= s.lower().strip()[0] <= 'c' or s.lower().strip()[0] in string.punctuation:
            self.firstNum = True
        return int(''.join([str(ord(c)).zfill(3) for c in s.lower().strip()]))

    # Message encryption
    def messageEncryption(self, s, e, n):

        print("Message: " + s)
        number = self.textToAscii(s)
        print("ASCII: " + str(number))
        self.c = pow(number, e, n)
        print("Encrypted message: " + str (self.c))

    def messageEncryptionNumber(self, number, e, n):
        self.c = pow(number, e, n)
        print("Encrypted message: " + str (self.c))

    def messageEncryptionText(self, s, e, n):

        print("Message: " + s)
        number = self.textToNumber(s)
        self.c = pow(number, e, n)
        print("Encrypted message: " + str (self.c))

    #Section C
    # Message decryption
    def messageDecryption(self):
         print("D: " + str(self.d))
         decrypMessage = pow(self.c, int(self.d), self.n)
         print("Decrypted: " + str(decrypMessage))
         return str(decrypMessage)

    def messageDecryptionMoodle(self, m):
         print("Message received: " + str(m))
         decrypMessage = pow(m, int(self.d), self.n)
         print("Decrypted message: " + str(decrypMessage))
         return str(decrypMessage)

    # ASCII to text
    def asciiToText(self):
        m = ''
        c_str = self.messageDecryption()

        if self.firstNum == True:
            m += chr(int(c_str[0:2]))
            for i in range(2, len(c_str), 3):
                m += chr(int(c_str[i:i + 3]))
        else:
            for i in range(0, len(c_str), 3):
                m += chr(int(c_str[i:i + 3]))

        print("Decrypted message: "+ m)

    def textToNumber(self,text):
        text = text.lower()
        num = 0
        for i, char in enumerate(reversed(text)):
            num += (ord(char) - ord('a') + 1) * (26 ** i)
        print ("Num: ", str(num))
        return int(num)

    def numberToText(self,num):
        text = []
        while num > 0:
            num -= 1  # Ajuste por base 1
            text.append(chr((num % 26) + ord('a')))
            num //= 26
        print("Text: ", ''.join(reversed(text)))