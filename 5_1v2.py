#1
"""Создайте класс StringVar для работы со строковым типом данных,
содержащий методы set() и get(). Метод set() служит для изменения
содержимого строки, get() – для получения содержимого строки. Создайте
объект типа StringVar и протестируйте его методы. """

class StringVar:
    def __init__(self, initial_string=""):
        self.string = initial_string
    
    def set(self):
        self.string = str(input("Введите строку: "))
        return self.string
    
    def get(self):
        return self.string

obj = StringVar("123")

print(obj.get())
print(obj.set())


#2
"""Создайте класс точка Point, позволяющий работать с координатами (x, y).
Добавьте необходимые методы класса."""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_coordinates(self):
        return (self.x, self.y)
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def get_distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)
    
    def vector(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        angle = math.degrees(angle_rad)
        
        return (length, angle_rad)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        return self