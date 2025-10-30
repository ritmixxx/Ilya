1.6
t = int(input("Введите число №1: "))
v = int(input("Введите число №2: "))
x = int(input("Введите число №3: "))
y = int(input("Введите число №4: "))
print(f'а) 5 10 \t б) 100 {t}\tв) {x} 25')
print(f'   7 см \t    1949 {v} \t   {x} {y}')
1.7
a = int(input("Введите число №1: "))
b = int(input("Введите число №2: "))
x = int(input("Введите число №3: "))
y = int(input("Введите число №4: "))
print(f'а) 2 кг \t б) {a} 1 \t в) {x} {y}')
print(f'   13 17 \t    19 {b} \t    5 {y}')
2.1
x = float(input("Введите значение x: "))
y = 17 * x**2 - 6 * x + 13
print(f"Для x = {x} значение функции y = {y}")
2.1
a = float(input("Введите значение a: "))
y = 3 * a**2 + 5 * a - 21
print(f"Для a = {a} значение функции y = {y}")
2.2
def fun(a):
    return (a ** 2 + 10) / (a ** 2 + 1) ** (1 / 2)
2.3
import math
def A(a):
    return math.sqrt((2 * a + math.sin(abs(3 * a))) / 3.56)
2.3
import math
def B(x):
    return math.sin((3.2 + math.sqrt(1 + x)) / (abs(5 * x)))
2.4
side = float(input("Введите длину стороны квадрата: "))
perimeter = 4 * side
print(f"Периметр квадрата равен {perimeter}")
2.5
radius = float(input("Введите радиус окружности: "))
diameter = 2 * radius
print(f"Диаметр окружности равен {diameter}")
2.6
import math
R = 6350  # радиус Земли в км
h = float(input("Введите высоту над Землей в километрах: "))
d = math.sqrt(2 * R * h + h ** 2)
print(f"Расстояние до линии горизонта: {d:.2f} км")
2.7
a = float(input("Введите длину ребра куба: "))
volume = a**3
lateral_area = 4 * a**2
print(f"Объём куба: {volume}")
print(f"Площадь боковой поверхности куба: {lateral_area}")
