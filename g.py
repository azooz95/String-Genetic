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

    def fittness(self, solution, c_solution):
        solution = np.array(solution)
        c_solution = np.array(c_solution)
        a = np.extract(solution == c_solution, c_solution)
        return sum(a)/len(solution)


class Strng():
    pass

a = Genetic()
print(a.fittness([1,0,1,1] , [1,1,0,1]))