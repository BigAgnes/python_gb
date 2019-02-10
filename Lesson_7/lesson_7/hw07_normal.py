'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''

class Matrix(list):
    def __init__(self, matrix):
        self.matrix = matrix
        self.x = matrix[0]
        self.y = matrix[1]
        self.z = matrix[2]
    def print(self):
        for el in self.matrix:
            print (el)
    def __add__(self, other):
        return ((self.x + other.x), (self.y + other.y), (self.z + other.z))

g1 = Matrix([[1, 2, 3], [5, 4, 6], [8, 9, 7]])
g2 = Matrix([[3, 2, 1], [6, 4, 5], [7, 9, 8]])
print(g1.print())
g3 = g1 + g2
print(g3)


