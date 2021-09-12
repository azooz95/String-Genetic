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
    def __init__(self) -> None:
        self.all_data = []

    def init_population(self, number, no_binary = 4):
        self.all_data = np.random.randint(2, size=(number,no_binary))
        return self.all_data 

    def adding_todata(self, data):
        self.all_data = np.concatenate((self.all_data, data), axis=0)
        return self.all_data

    def fittness(self, solution, c_solution):
        solution = np.array(solution)
        c_solution = np.array(c_solution)
        a = np.extract(solution == c_solution, c_solution)
        return sum(a)/len(solution)

    def selection(self):
        pass

    def crossover(self, f_par, s_par, singl_point = 2):
        

class Strng():
    pass

a = Genetic()
print(a.fittness([1,0,1,1] , [1,1,0,1]))