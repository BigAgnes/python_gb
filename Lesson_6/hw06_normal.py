'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''
import math
class Triangle():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.b_x = b_x
        self.c_x = c_x
        self.a_y = a_y
        self.b_y = b_y
        self.c_y = c_y
# сначала найдем длины сторон треугольниа по формуле AB = √(xb - xa)2 + (yb - ya)2
        self.AB = round(math.sqrt(int(math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),1)
        self.AC = round (math.sqrt(int (math.fabs(((c_y - a_y)**2) + ((c_x - a_x)**2)))),1)
        self.CB = round (math.sqrt(int (math.fabs(((b_y - c_y)**2) + ((b_x - c_x)**2)))),1)

#периметр

    def perimetr(self):
        self.perimetr = round((self.AB + self.AC + self.CB),1)
        return self.perimetr
#площадь

    def ploshad(self):
        self.perimetr_1 = self.perimetr / 2
        self.ploshad = round(math.sqrt(self.perimetr_1 * (self.perimetr_1 - self.AB)*(self.perimetr_1 - self.AC)*(self.perimetr_1 * self.CB)), 1)
        return self.ploshad

    def vysota(self):
        self.ploshad = self.ploshad * 2
        self.vysota = round((self.ploshad / self.AC),1)
        return self.vysota


my_triangle = Triangle(3, 3, 5, 8, 6, 4)

print("Длина стороны AB = {}, AC = {}, CB = {}".format(my_triangle.AB, my_triangle.AC, my_triangle.CB))
print("Периметр треугольника равен {}".format(my_triangle.perimetr()))
print("Площадь треугольника равна {}".format(my_triangle.ploshad()))
print("Высота треугольника равна {}".format(my_triangle.vysota()))

