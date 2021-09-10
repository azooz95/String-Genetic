class Genetic():
    def __new__(self, binary = True, strng=False):
        self.binary = binary
        self.strng = strng
        if self.strng:
            return Strng()
        elif self.binary:
            return Binary()

class Binary():
    def population(self, population):
        return "this is the population: " + population

class Strng():
    pass

a = Genetic()
print(a.population('hi'))