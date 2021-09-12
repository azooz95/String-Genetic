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

    def data(self):
        return self.all_data

    def adding_todata(self, data):
        self.all_data = np.concatenate((self.all_data, data), axis=0)
        return self.all_data

    def fittness(self, solution, c_solution):
        solution = np.array(solution)
        c_solution = np.array(c_solution)
        a = np.extract(solution == c_solution, c_solution)
        return sum(a)/len(solution)

    def selection(self, solution):
        a = {index: round(10*self.fittness(solution,i)) for index,i in enumerate(self.data())}
        # s = sum(a.values())
        # p = 0
        # selected_one = np.array([0,0,0,0])
        # print("Sum of: ", s, "r: ", r)
        # for i in range(0,r):
        #     p = p + a[i]
        #     if s<p:
        #         selected_one = self.data()[i]
        #         break
        #     if i == r-1:
        #         for j in range(r-1,len(a)):
        #             print(str(self.data()[i])+": ",p)
        #             p = p + a[j]
        #             if s<p:
        #                 selected_one = self.data()[i]
        #                 break
        #         break
        #     print(str(self.data()[i])+": ",p)
        # print(selected_one)
        
        probolity = []
        for i in a:
            probolity = probolity + ([i]*a[i])
        r = np.random.randint(0,len(probolity))
        ind = probolity[r]
        select_par = self.data()[ind]
        return select_par

    def crossover(self, f_par, s_par, singl_point = 2):
        f_par_1, f_par = f_par[:singl_point], f_par[singl_point:]
        s_par_1, s_par = s_par[:singl_point], s_par[singl_point:]
        return s_par_1+f_par, f_par_1+s_par

    def muetation(self, new_parent):
        a = np.random.randint(0, len(new_parent))
        new_parent[a] = int(not bool(new_parent[a]))
        return new_parent

class Strng():
    pass

a = Genetic()
t = a.init_population(7)
print(a.data())
g = a.muetation(np.array([1,1,1,1]))
print(g)
