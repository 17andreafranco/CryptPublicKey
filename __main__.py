from sympy.crypto import rsa_private_key
from RSA import cryptRSA
from DiffieHellman import cryptDH
from DigitalSignatureRSA import cryptDS

def __main__():
    rsa = cryptRSA(65537,10000000000, 15000000000)
    dh = cryptDH()
    ds = cryptDS()

    print("---------------- My key ----------------")
    rsa.publicPrivateKey()

    print("\n---------------- Moodle encrypt ----------------")

    rsa.messageEncryptionNumber(104111108097, 5, 80000118934008630271)
    rsa.messageEncryptionText("hola", 5, 80000118934008630271)

    print("\n---------------- Moodle decrypt ----------------")
    rsa.messageDecryptionMoodle(87131147427545718790)
    rsa.numberToText(int(rsa.messageDecryptionMoodle(142303695374553002716)))

    print("\n---------------- DH ----------------")
    dh.calculA(17)
    dh.sherdKey(17, 62)

    print("\n---------------- DS ----------------")
    ds.digitalSignature("adios", 5, 80000118934008630271)
    ds.certificateDS(106643168623153649274, 87131147427545718790)

if __name__ == '__main__':
    __main__()