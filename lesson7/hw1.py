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
'''переделала по итогк товоего разбора'''
class Matrix():
    def __init__(self, list_1):
        self.new_list = list_1

    def __str__(self):
        return '\n'.join(map(str, self.new_list))
    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.new_list)):
            new_matrix.append([])
            for j in range(len(self.new_list[0])):
                new_matrix[i].append(self.new_list[i][j] + other.new_list[i][j])
        return Matrix(new_matrix)

a = [[-1,2],
     [3,5],
     [2,5]]
b = [[5, 2],
     [1,2],
     [2, 3]]
mtrx = Matrix(a)
new_mtrx = Matrix(b)
print(mtrx + new_mtrx)
