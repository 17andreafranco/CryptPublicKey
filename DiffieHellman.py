import random

class cryptDH(object):
    def __init__(self):
       self.p = 7883
       self.g = 2

    def calculA(self, a):
        num = pow(self.g, a, self.p)
        print(str(num))
        return num

    def sherdKey(self, a, b):
        ab = a * b
        sherdKey = pow(self.g, ab, self.p)
        print("Sherd Key: ", sherdKey)