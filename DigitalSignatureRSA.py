import random
from RSA import cryptRSA

rsa = cryptRSA(65537, 10000000000, 15000000000)

class cryptDS(object):
    def __init__(self):
        self.n = None
        self.e = None
        self.d = None

    def publicPrivateKeys(self):
        rsa.publicPrivateKey()

        self.n = rsa.getN()
        self.e = rsa.getE()
        self.d = rsa.getD()

    def digitalSignature(self, m, e, n):
        self.publicPrivateKeys()
        num = rsa.textToNumber(m)

        c = pow(num, e, n)
        hash_value = c % 1000003

        sig = pow(hash_value, int(self.d), n)

        print("\nPublic key:", e)
        print("Private key:", str(self.d))
        print("Crypt message:", c)
        print("Digital signature:", sig)

    def certificateDS(self, sig, r_emissor):
        r = pow(sig, self.e, self.n)

        if r == r_emissor:
            print("\nSignature match")
        else:
            print("\nSignature Mismatch")
            print(r)
