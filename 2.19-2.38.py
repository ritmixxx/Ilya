2.19
import math

def X(a, b):
    return (2 / (a ** 2 + 25) + b) / (b ** (1 / 2) + (a + b) / 2)
def Y(a, b):
    return (abs(a) + 2 * math.sin(b)) / (5.5 * a)
2.20
import math
def A(e, f, g):
    return math.sqrt((abs(e - 3 / f)) ** 3 + g)
2.20
def B(e, h):
    return math.sin(e) + (math.cos(h)) ** 2
2.20
def C(g, e, f):
    return 33 * g / (e * f - 3)
2.21
import math
def A(e, f):
    return (e + f / 2) / 3
2.21
def B(h, g):
    return abs(h ** 2 - g)
2.21
def C(g, h, e):
    return ((g - h) ** 2 - 3 * math.sin(e)) ** (1 / 2)
2.22
def PerDiag(a, b):
    Perimetr = a * 2 + b * 2
    Diag = (a ** 2 + b ** 2) ** (1 / 2)

    return Perimetr, Diag
2.23
def PerDiag(a, b):
    Perimetr = a * 2 + b * 2
    Diag = (a**2 + b**2) ** (1 / 2)

    return Perimetr, Diag
2.24
def MathOps(a, b):
    summ = a + b
    razn = a - b
    proizv = a * b
    chast = a / b

    return summ, razn, proizv, chast

2.25

def VSparal(a, b, c):
    vol = a * b * c
    Sbok1 = a * b
    Sbok2 = b * c
    Sbok3 = a * c

    return vol, Sbok1, Sbok2, Sbok3
2.26
class Point:
    def init(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc_dist(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Дай мне объект класса Точка")

        return ((self.x - another_point.x)**2 + (self.y - another_point.y)**2) ** (1 / 2)
2.27
import math

a = float(input("Введите длину верхнего основания (a): "))
b = float(input("Введите длину нижнего основания (b): "))
h = float(input("Введите высоту трапеции (h): "))

if b >= a >= 0 and h > 0:
    c = math.sqrt(h**2 + ((b - a)/2)**2)
    perimeter = a + b + 2 * c
    print("Периметр равнобедренной трапеции:", perimeter)
else:
    print("Ошибка: проверьте, что основания неотрицательны, a ≤ b, и высота положительна.")
2.28
import math


def STrap(O1, O2, angle):
    if O1 > O2:
        O1, O2 = O2, O1

    while angle > 360:
        angle -= 360

    angle = angle * math.pi / 180

    return 0.5 * (O2**2 - O1**2) * math.tan(angle)
2.29
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc_dist(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Дай мне объект класса Точка")

        return ((self.x - another_point.x)**2 + (self.y - another_point.y)**2) ** (1 / 2)


class Triangle:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

        self.a = Point.calc_dist(self.A, self.B)
        self.b = Point.calc_dist(self.B, self.C)
        self.c = Point.calc_dist(self.A, self.C)

    @property
    def Perim(self):
        return self.a + self.b + self.c

    @property
    def Square(self):
        p = self.Perim / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)

2.30
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc_dist(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Дай мне объект класса Точка")

        return ((self.x - another_point.x)**2 + (self.y - another_point.y)**2) ** (1 / 2)


class Triangle:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

        self.a = Point.calc_dist(self.A, self.B)
        self.b = Point.calc_dist(self.B, self.C)
        self.c = Point.calc_dist(self.A, self.C)

    @property
    def Perim(self):
        return self.a + self.b + self.c

    @property
    def Square(self):  
        p = self.Perim / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)


class Quadrangle:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.a = Point.calc_dist(self.A, self.B)
        self.b = Point.calc_dist(self.B, self.C)
        self.c = Point.calc_dist(self.D, self.C)
        self.d = Point.calc_dist(self.A, self.D)

    @property
    def Square(self):
        A1 = Triangle(self.A, self.B, self.D)
        A2 = Triangle(self.A, self.D, self.C)

        return A1.Square + A2.Square
2.31
x = float(input("Стоимость конфет за 1 кг: "))
y = float(input("Стоимость печенья за 1 кг: "))
z = float(input("Стоимость яблок за 1 кг: "))
def cost(nx, ny, nz):
    return nx * x + ny * y + nz * z
2.32
def cost_pc(number):
    monit = 2
    block = 4  
    klava = 3
    mouse = 1
    return (monit + block + klava + mouse) * number
2.33
def averege(Tanya, Mitya):
    av = (int(Tanya) + int(Mitya)) / 2
    print(f'Средний возраст: {av}')
    print(f'Возраст Тани отличается от среднего на {abs(int(Tanya) - av)}')
    print(f'Возраст Мити отличается от среднего на {abs(int(Mitya) - av)}')
2.34
def meet_time(V1=60, V2=60, S=100):
    return f'Через {(V1 + V2) / S} ч автомобили встретятся'
2.35
def dist_30mins(V1=80, V2=60):
    if V2 >= V1:
        print("V1 должно быть больше V2")
    else:
        return f'через 30 минут между автомобилями будет {(V1 - V2) / 0.5} км'
2.36
def temp_converter(Celsium):
    print(f'{(Celsium * 1.8) + 32} по Фаренгейту')
    print(f'{Celsium + 273.15} по Кельвину')
2.37
def temp_conv(Farenheit):
    return f'{(Farenheit - 32) / 1.8} градусов Цельсия'
2.38
def mathops(a, b):
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b}')
    print(f'({a} + {b}) / 2 = {(a + b) / 2}')
