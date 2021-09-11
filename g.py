import numpy as np

class Genetic():
    def __new__(self, binary = True, strng=False):
        self.binary = binary
        self.strng = strng
        if self.strng:
            return Strng()
        elif self.binary:
            return Binary()

class Binary():
    def init_population(self, number, no_binary = 4):
        return np.random.randint(2, size=(number,no_binary))

    def 
class Strng():
    pass

a = Genetic()
print(a.init_population(6))