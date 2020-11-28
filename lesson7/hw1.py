from copy import deepcopy
class Matrix():
    new_list = []
    def __init__(self, list_1):
        self.new_list = list_1

    def __str__(self):
        return '\n'.join(map(str, self.new_list))
    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.new_list)):
            for j in range(len(self.new_list[i])):
                new_matrix[i][j] = self.new_list[i][j] + other.new_list[i][j]
        return new_matrix
mt = Matrix([[-1,2],[3,5],[2,5]])
new_mt = Matrix([[5, 2], [1,2], [2, 3]])
print(mt.__add__(new_mt))
'''в функции add запуталась'''